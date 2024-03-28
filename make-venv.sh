#!/bin/bash
# Tyler LaBree
# Northern Illinois University

source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
setup dunesw v09_78_03d01 -q e20:prof
setup dune_plot_style v01_00

python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install pyroot jupyterlab urllib3==1.26.6

