#!/bin/bash

# the Hadoop-streaming enviroment does not read the standard bash startup files,
# so we must use a wrapper to explicitly set up the modules environment and load 
# the relevant modules

. /etc/profile.d/modules.sh
module load python/gnu/2.7.11
python Code/reduce3.py
