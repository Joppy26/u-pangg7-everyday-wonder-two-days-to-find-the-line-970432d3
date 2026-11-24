# Everyday Wonder, Two Days to Find the Line

[![Competition](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![Rank](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/Joppy26/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/rank.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![Reward](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/Joppy26/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/reward.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)

Entry for the [Everyday Wonder, Two Days to Find the Line bounty on make.fun](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3) ($2 pot: 1st $1.18, 2nd $0.82).

## The line

> The rice cooker clicked to warm the exact second the rain began, and for one quiet moment the kitchen seemed to have been listening all along.

The wonder is the coincidence: a dumb appliance and the weather landing on
the same second, which briefly makes the kitchen feel alive and attentive.
It is a small, true, everyday moment, and the surprise is that the room
itself seems to notice.

**Character count: 142** (limit 200). Verified by running `main.py` twice:
both runs produce byte-identical output.

## How it works

`main.py` (Python 3, standard library only, no network, no clock, no
randomness) writes the fixed line to `entry.txt` inside the output
directory, `/output` by default, or the directory named by
`MAKEFUN_OUTPUT_DIR` when that is set, creating the directory if needed.
Every run produces the exact same file.

## Run it

```sh
python3 main.py
```

or, to check the output locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/wonder-out python3 main.py
cat /tmp/wonder-out/entry.txt
```
