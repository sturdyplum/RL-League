# RL-League

## Our goal

Trying to create a system to easily train RL agents in a league similar to how it was done in the alphastar environment

## Setup

First start up a virtualenv

```bash
python3 -m virtualenv .
source bin/activate
```

Then install the requirements

```bash
pip install -r requirements.txt
```

Build proto definitions

```bash
./build_proto.sh
```

Install proto build package

```bash
pip install -e .
```

Run the RL League

```bash
python -m rlleague
```
