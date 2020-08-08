# RL-League

## Our goal
Trying to create a system to easily train RL agents in a league similar to how it was done in the alphastar environment

## Setup
First start up a virtualenv
```
python3 -m virtualenv .
source bin/activate
```

Then install the requirements
```
pip install -r requirements.txt
```

Build proto definitions
```
./build_proto.sh
```

Install proto build package
```
pip install -e .
```

Run the RL League
```
python -m rlleague
```
