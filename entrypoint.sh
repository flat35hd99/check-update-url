#!/bin/bash

PYTHON=python

path=`readlink -f "${BASH_SOURCE:-$0}"`
dir=`dirname $path`
source ${dir}/.env

${PYTHON} ${dir}/main.py
