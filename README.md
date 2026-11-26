# news-image-20261125

One sheet, every story that mattered. This repo renders a fictional 1024×1024
newspaper front page — *THE WORLD*, dated Wednesday 25 November 2026 — with a
Pillow-based generator (`gen_news.py`, run once at build time). The finished
image ships in the repo as `entry.png`; nothing is drawn at runtime.

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/RobertAlbert11/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/RobertAlbert11/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

## Running it

```sh
python3 main.py
```

The runner just hands over the committed `entry.png`: it copies the file into
`$MAKEFUN_OUTPUT_DIR` (default `/output`), checks the copy matches the source
byte-for-byte, fsyncs it, and exits non-zero on any failure. Only the Python
standard library is required.

## What's on the page

A centred masthead with volume/edition folio and price, a dominant hero panel
on China flying its first foreign astronaut to Tiangong (Shenzhou-24) with a
rocket illustration, a disciplined six-card grid carrying datelines, bylines
and page folios (Ukraine's leaked 500,000-dead tally, the ICJ Rohingya
genocide ruling, the COP31 collapse in Antalya, the US Huawei conviction,
Tesla–SpaceX merger committees, Miss Universe 2026), and a bottom wire ticker
with the Mississippi plane crash, the CIA open-source breach, Bangladesh
garment wages, and US–Iran funding through January.

## License

MIT — see `LICENSE`.
