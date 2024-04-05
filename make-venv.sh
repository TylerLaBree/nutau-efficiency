#!/bin/bash
# Tyler LaBree
# Northern Illinois University

source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
setup dunesw v09_78_03d01 -q e20:prof

python3 -m venv venv
source venv/bin/activate
venv/bin/python3.9 -m pip install --upgrade pip
venv/bin/python3.9 -m pip install pyroot jupyterlab urllib3==1.26.6 matplotlib scipy

export DUNE_PLOT_STYLE_LATEST_TAG=`curl --silent "https://api.github.com/repos/DUNE/dune_plot_style/releases" | jq -r 'map(select(.prerelease == false)) | first | .tag_name'`
wget --no-check-certificate https://github.com/DUNE/dune_plot_style/archive/refs/tags/${DUNE_PLOT_STYLE_LATEST_TAG}.tar.gz -O dune_plot_style.tar.gz
tar -xvzf dune_plot_style.tar.gz
cd dune_plot_style-01_00
../venv/bin/python3.9 -m pip install .
cd ..
