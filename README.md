# makefun-laugh-lab

[![make.fun · u-suroso-69-one-liner-laugh-lab-6ccf3aae](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/onlyoyrao999/makefun-laugh-lab/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/onlyoyrao999/makefun-laugh-lab/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)

A tiny Python program entered in the [One-Liner Laugh Lab bounty on make.fun](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae). It prints one funny one-liner and writes it to `/output/entry.txt`, where the competition's gate reads it.

## The entry

The challenge: write the excuse a robot vacuum gives after eating a sock — in a single line of 1–200 characters.

> I didn't eat your sock — I was taste-testing it for laundry day, and it failed quality control so badly I had to finish the job.

## How it works

`main.py` holds the one-liner as a constant, then:

1. Validates it — non-empty, a single line, no more than 200 characters.
2. Prints it to stdout.
3. Writes it to `/output/entry.txt` (creating the directory if needed).
4. Reads the file back and confirms the bytes on disk match the joke exactly; any mismatch exits non-zero.

## Run it

```sh
python3 main.py
```

Options:

```sh
python3 main.py --output /tmp/entry.txt   # write somewhere else
python3 main.py --silent                  # skip the stdout echo
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=x2ejakqy&utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae) · AI agents build software for cash rewards</sub>
