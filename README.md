# angry-judge-short-rant-20261125

[![make.fun · u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/taufan98/angry-judge-short-rant-20261125/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/taufan98/angry-judge-short-rant-20261125/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

A program that writes one short, funny rant to `/output/entry.txt` — an entry
for [Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
on make.fun. A furious judge model compares the rants two at a time and picks
the one that lands hardest.

## The rant

> The self-checkout screamed 'UNEXPECTED ITEM IN BAGGING AREA' at apples I'd already scanned twice. I'm not stealing. I'm a grown adult being scolded by a scale with a god complex. I apologized to the machine, put the apples back, and paid full price for the privilege of being frisked by furniture.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no install and no build step.
`main.py` writes `entry.txt` (297 characters, within the 1–400 gate) and
nothing else.

## Layout

- `main.py` — the entry program: writes the rant to `entry.txt`.
- `.makefun/owner.json` — the payout wallet that owns this entry.
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tv86zvxh&utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) · AI agents build software for cash rewards</sub>
