# news-image-20261125

This is my take on 25 November's world news, set as a single printed sheet:
*THE WORLD*, Wednesday 25 November 2026, rendered at 1024×1024 with a Pillow
generator (`gen_news.py`, run once at build time). The finished page is
committed as `entry.png`; nothing is drawn at runtime.

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

A dark masthead band with volume folio, edition and price; a hero panel on
China flying its first foreign astronaut to Tiangong with a rocket drawing and
a color-coded region legend; a dot-map of the five covered regions; a dense
three-column grid of twelve story cards, each with a dateline kicker, blurb
and a `via <agency> · HH:MM UTC` source line (Ukraine's leaked 500,000-dead
tally, the ICJ Rohingya genocide ruling, the COP31 collapse in Antalya, the
US Huawei conviction, Tesla–SpaceX merger committees, Miss Universe 2026,
Kospi −6.2% on AI doubts, the UK energy cap rising 26% to £2,166, the Cairo
fires, the flooded West Java gold mine, US tariffs on 14 economies, the
Mississippi plane crash probe); a "MORE FROM THE WIRE" band of timestamped
one-liners (Bangladesh garment wages +36%, the UK energy cap, the Cairo tanker
fire, the West Java mine, US tariffs, the Mississippi docket, US–Iran funding);
a folio footer.

## License

MIT — see `LICENSE`.
