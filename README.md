# Cresent-Retro

A Game Boy Color program made with [8bitworkshop](https://8bitworkshop.com/redir.html?platform=gb.color&file=siegegame.c).

## Build and run

In VS Code with the 8bitworkshop extension, open `siegegame.c` and click **Run**.

From VS Code's integrated terminal, in this folder (turn on the
`8bitworkshop.terminalCommand` setting first):

```sh
# compile to a ROM
8bws build siegegame.c -o siegegame.gbc
# run without a window for 120 frames, and save a screenshot
8bws run siegegame.c --frames 120 --png screen.png
# all commands and options
8bws help
```

Add `--json` for machine-readable output.
