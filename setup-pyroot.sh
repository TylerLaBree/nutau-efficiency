#!/bin/bash
# Tyler LaBree
# Northern Illinois University

# Setup the latest versions of root and dune-plot-style
source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
source venv/bin/activate
#setup root v6_26_06b -q e26:p3913:prof
setup dunesw v09_78_03d01 -q e20:prof
setup dune_plot_style v01_00
#source $ROOTSYS/bin/thisroot.sh

# Teach ROOT about the dune-plot-style include directory
export ROOT_INCLUDE_PATH=$DUNE_PLOT_STYLE_INC:$ROOT_INCLUDE_PATH
