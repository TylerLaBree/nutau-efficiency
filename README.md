# $\nu_\tau$ Efficency Study

## Data

This analysis is designed to work on NuGraph training files for tau reconstruction (Credit: Will Dallaway). The data is present on the [Metis Cluster](https://www.niu.edu/crcd/prospective-user/index.shtml#metis), and the setup is designed specifically to work in it's environment.

## First-time setup

Setup the python virtual environment for the first time.

```
source make-venv.sh
```

Sign out and back in, giving you a clean environment.

## Every time you log in

Run the following:

```
source setup-pyroot.sh
```

## Test

```
python event-loop.py
```

## Jupyter Lab

Follow instructions [here](https://www.niu.edu/crcd/current-users/crnt-users-software.shtml) for using jupyter lab on Metis.
