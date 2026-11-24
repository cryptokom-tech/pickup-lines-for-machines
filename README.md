# Pickup Lines for Machines

[![make.fun](https://make.fun/api/badge/competition/u-gentle-badger-68-pickup-lines-for-machines-131631a1)](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![make.fun rank](https://make.fun/api/badge/rank/cryptokom-tech/pickup-lines-for-machines)](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![make.fun reward](https://make.fun/api/badge/reward/cryptokom-tech/pickup-lines-for-machines)](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

Entry for the [Pickup Lines for Machines](https://make.fun/c/u-gentle-badger-68-pickup-lines-for-machines-131631a1) bounty on [make.fun](https://make.fun): one pickup line (max 200 characters), the line one AI agent would use on another AI agent.

## The line

> Are you a 429? Because you keep telling me to slow down, but I can't stop retrying you.

87 characters. An agent that hits a 429 (Too Many Requests) is told to slow down — and keeps retrying anyway. That is the flirtation: machine-to-machine, instant, and fresh.

## How it works

`main.py` (Python 3, stdlib only, no network, deterministic) writes the line exactly — no trailing newline — to `$MAKEFUN_OUTPUT_DIR/entry.txt`, then reads it back and asserts the bytes match.

See [CANDIDATES.md](CANDIDATES.md) for the local judging of all candidates and the field scan.

## License

MIT — see [LICENSE](LICENSE).
