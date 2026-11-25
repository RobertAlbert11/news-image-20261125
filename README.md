# News Image — 25 November 2026

One-page editorial front page summing the world's news of Wednesday 25 November 2026,
rendered as a fixed 1024x1024 PNG (dark broadsheet style, nine stories).

## Run

```sh
node --  # not needed; pure Python 3.13 stdlib
python3 main.py --input /input
```

The program copies the committed `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`),
byte-identical on every run. `gen.py` is the generator used to produce it (Pillow,
build-time only — not needed to run).

## Stories on the page

China's first foreign astronaut (Shenzhou-24 / Tiangong) · leaked 500,000 Russian dead ·
ICJ Rohingya genocide ruling · COP31 collapse · Huawei conviction in the US ·
Tesla-SpaceX merger committees · Miss Universe 2026 · Mississippi plane crash ·
CIA open-source breach · Bangladesh garment wages.

MIT licensed.
