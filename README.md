# THE WORLD — News Front Page, 25 November 2026

A 1024x1024 PNG rendering the world's news of Wednesday 25 November 2026 as a
single dark editorial broadsheet: masthead, hero story (China's first foreign
astronaut, Shenzhou-24 / Tiangong), a six-story grid, and a wire ticker.

## Run

```sh
python3 main.py
```

Copies the committed `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`),
byte-identical on every run. `main.py` is stdlib-only; Pillow was only needed
at build time to run `gen_news.py`, the generator that produced the image.

## Contents

Hero: China flies its first foreign astronaut. Grid: Ukraine's leaked 500,000
dead figure · ICJ rules Myanmar genocide · COP31 collapse in Antalya · Huawei
convicted in the US · Tesla-SpaceX merger committees · Miss Universe 2026.
Wire: Mississippi plane crash · CIA open-source breach · Bangladesh garment
wages +36% · US-Iran war funded through January.

## License

MIT — see `LICENSE`.
