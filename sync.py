"""Sync files to the Thumby browser editor using browser localStorage.

The browser editor is normally run with Chrome remote debugging enabled, for example:

Windows:
    "C:\Program Files\Google\Chrome\Application\chrome.exe" ^
      --remote-debugging-port=9222 https://code.thumby.us/

Then run, for example:
    python sync.py --source HelloWorld.py --destination /Games/HelloWorld/HelloWorld.py
    python sync.py --source ./my_games --destination /Games

The script watches files for changes and writes their contents to EditorPathN and
EditorValueN in localStorage. Selenium must be installed:
    python -m pip install selenium
"""

from __future__ import annotations

import argparse
import os
import signal
import sys
import time
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="VS Code file watcher for code.thumby.us")
    parser.add_argument("source", nargs="?", default=".", help="File or directory to watch")
    parser.add_argument("--destination", default=None, help="Browser path, or root path for a directory")
    parser.add_argument("--url", default="https://code.thumby.us/", help="Thumby editor URL")
    parser.add_argument("--debug-port", type=int, default=None,
                        help="Attach to Chrome launched with --remote-debugging-port")
    parser.add_argument("--profile", default=None,
                        help="Optional Chrome user-data directory")
    parser.add_argument("--interval", type=float, default=0.5, help="Polling interval in seconds")
    parser.add_argument("--exclude", action="append", default=[],
                        help="Substring to exclude (repeatable)")
    return parser.parse_args()


def browser_driver(url: str, debug_port: int | None, profile: str | None):
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
    except ImportError as exc:
        raise RuntimeError("Selenium is not installed. Run: python -m pip install selenium") from exc

    options = Options()
    if profile:
        options.add_argument(f"--user-data-dir={profile}")

    if debug_port is not None:
        options.add_experimental_option("debuggerAddress", f"127.0.0.1:{debug_port}")

    try:
        if sys.platform.startswith("win") and os.environ.get("PROGRAMFILES"):
            chrome_path = Path(os.environ["PROGRAMFILES"]) / "Google/Chrome/Application/chrome.exe"
            if chrome_path.exists():
                options.binary_location = str(chrome_path)

        driver = webdriver.Chrome(options=options)
    except Exception as exc:
        raise RuntimeError(
            "Chrome could not be started. Install Chrome, install Selenium, or use --debug-port."
        ) from exc

    driver.get(url)
    from selenium.webdriver.support.ui import WebDriverWait
    WebDriverWait(driver, 20).until(lambda d: d.execute_script("return window.location.hostname") == "code.thumby.us")
    return driver


def list_files(source: Path, exclusions: Iterable[str]) -> List[Path]:
    if source.is_file():
        return [source]
    if not source.exists():
        return []

    excluded = tuple(exclusions)
    files: List[Path] = []
    for root, dirs, names in os.walk(source):
        dirs[:] = [d for d in dirs if not d.startswith(".") and "__pycache__" not in d]
        for name in names:
            path = Path(root) / name
            if any(value and value in str(path) for value in excluded):
                continue
            if path.suffix.lower() in {".pyc", ".tmp", ".bak"}:
                continue
            files.append(path)
    return sorted(files, key=lambda p: p.as_posix().lower())


def browser_path_for(source: Path, source_root: Path, destination: str | None) -> str:
    if source.is_file():
        if destination:
            destination = destination.replace("\\", "/").strip("/")
            if destination.endswith("/Games") or destination.startswith("Games/") or destination == "Games":
                return "/" + destination.rstrip("/") + "/" + source.name
            return "/" + destination
        return f"/Games/{source.stem}/{source.name}"

    root = source.resolve()
    rel = source_root.relative_to(root).as_posix() if source_root.is_file() else source_root.relative_to(root).as_posix()
    prefix = destination or f"/Games/{root.name}"
    prefix = prefix.replace("\\", "/").rstrip("/")
    if not prefix.startswith("/"): prefix = "/" + prefix
    return prefix + "/" + rel


def read_snapshot(files: List[Path], source: Path, destination: str | None) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for path in files:
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = path.read_text(encoding="utf-8", errors="replace")
        result[browser_path_for(source, path, destination)] = content
    return result


def sync_to_browser(driver, snapshot: Dict[str, str]) -> None:
    items: List[Tuple[str, str]] = sorted(snapshot.items(), key=lambda item: item[0].lower())
    script = """
const items = arguments[0];
for (const key of Object.keys(localStorage)) {
    if (/^Editor(Path|Value)\\d+$/.test(key)) localStorage.removeItem(key);
}
items.forEach(([path, value], index) => {
    localStorage.setItem('EditorPath' + index, path);
    localStorage.setItem('EditorValue' + index, value);
});
localStorage.setItem('EditorCount', String(items.length));
return items.length;
"""
    count = driver.execute_script(script, items)
    driver.refresh()
    print(f"Synced {count} file(s) to EditorPath0...EditorPath{count - 1}", flush=True)


def main() -> int:
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    if not source.exists():
        print(f"Source not found: {source}", file=sys.stderr)
        return 2

    print("Connecting to Chrome...", flush=True)
    try:
        driver = browser_driver(args.url, args.debug_port, args.profile)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    last: Dict[str, str] | None = None
    exclusions = [str(source)] + args.exclude

    def stop(_sig=None, _frame=None):
        print("\nStopping sync.", flush=True)
        try:
            driver.quit()
        except Exception:
            pass
        raise SystemExit(0)

    signal.signal(signal.SIGINT, stop)

    print(f"Watching: {source}", flush=True)
    print("Press Ctrl+C to stop.", flush=True)

    try:
        while True:
            files = list_files(source, exclusions)
            snapshot = read_snapshot(files, source, args.destination)
            if snapshot != last:
                try:
                    sync_to_browser(driver, snapshot)
                    last = snapshot
                except Exception as exc:
                    print(f"Browser sync failed: {exc}", file=sys.stderr)
            time.sleep(args.interval)
    finally:
        if args.debug_port is None:
            try:
                driver.quit()
            except Exception:
                pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
