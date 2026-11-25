# news-image-20261125

A 1024×1024 PNG front page of a fictional broadsheet, *THE WORLD*, dated
Wednesday 25 November 2026. The image is fully deterministic: it was rendered
once with `gen_news.py` (Pillow, build-time only) and the finished file ships
in this repo as `entry.png`.

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/RobertAlbert11/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/RobertAlbert11/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

## Running it

```sh
python3 main.py
```

This copies the committed `entry.png` into `$MAKEFUN_OUTPUT_DIR`
(default `/output`). Every run produces the identical bytes; the script
verifies this with a byte comparison and fsyncs the file before exiting.
Only the Python standard library is needed to run it.

## What's on the page

A dark masthead with a red accent bar, a hero panel on China flying its first
foreign astronaut to Tiangong (Shenzhou-24), and a six-card story grid:
the leaked 500,000-dead Russian war tally, the ICJ Rohingya genocide ruling,
the COP31 collapse in Antalya, the US Huawei conviction, Tesla–SpaceX merger
committees, and Miss Universe 2026. A bottom wire ticker covers the Mississippi
plane crash, the CIA open-source breach, Bangladesh garment wages, and US–Iran
funding through January.

## License

MIT — see `LICENSE`.
