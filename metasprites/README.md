# metasprites

A NES program made with [8bitworkshop](https://8bitworkshop.com/redir.html?platform=nes&file=metasprites.c).

## Build and run

In VS Code with the 8bitworkshop extension, open `metasprites.c` and click **Run**.

From VS Code's integrated terminal, in this folder (turn on the
`8bitworkshop.terminalCommand` setting first):

```sh
# compile to a ROM
8bws build metasprites.c -o metasprites.nes
# run without a window for 120 frames, and save a screenshot
8bws run metasprites.c --frames 120 --png screen.png
# all commands and options
8bws help
```

Add `--json` for machine-readable output.
