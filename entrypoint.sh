#!/bin/bash

source $HOME/miniconda3/bin/activate
PYTHON=python

path=`readlink -f "${BASH_SOURCE:-$0}"`
dir=`dirname $path`
source ${dir}/.env

${PYTHON} ${dir}/main.py
