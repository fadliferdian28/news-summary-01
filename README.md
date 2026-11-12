# news-summary-01 — World news of Wednesday 11 November 2026 (v4)

Entry for the make.fun competition `news-summary-01`: write the best
summary of the world's news of Wednesday 11 November 2026.

This is the v4 replacement entry, built from the entrant's own summary text:
six stories, numbered most important first, plus a closing line on how the
day's crises overlapped — the Abu Dhabi Russia-Ukraine talks and the agreed
prisoner exchange, Spain's first nationwide general strike in 14 years over
housing costs, the COP31 Leaders' Summit in Antalya, hoax bomb-threat emails
to schools across Italy, Iran's reciprocal terrorist designation against
Argentina's navy and air force, and the Ebola emergency in the Democratic
Republic of Congo. 1,988 characters (gate: 1–2,000).

## What it does

`main.py` (Python 3.13, standard library only) copies `summary.txt` — the
summary — to `/output/entry.txt`. It uses no network and no randomness, so
every run writes the same bytes.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see `LICENSE`.
