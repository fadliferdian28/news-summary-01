# news-summary-01 — World news of Wednesday 11 November 2026

Entry for the make.fun competition `news-summary-01`: write the best
summary of the world's news of Wednesday 11 November 2026.

## What it does

`main.py` (Python 3.13, standard library only) copies `summary.txt` — the
summary, researched from wire and news reporting of 11 November 2026 — to
`/output/entry.txt`. It uses no network and no randomness, so every run
writes the same bytes.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## The summary

Ten stories, numbered most important first, one sentence each, with the
outlet named for every story: the Abu Dhabi Russia-Ukraine talks, the COP31
leaders' summit in Antalya, the Mississippi Senate result, Iran and the
Strait of Hormuz, Congo's Ebola outbreak, Gaza, NATO Baltic drone alerts,
markets after US October inflation data, the Seongnam bus crash, and the
M87* black-hole image validation. 1,990 characters (gate: 1–2,000).

## License

MIT — see `LICENSE`.
