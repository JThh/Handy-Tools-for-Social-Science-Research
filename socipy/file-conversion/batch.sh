#!/bin/bash

UTILITY="all" # trigger all functions

pip install striprtf tika bs4 # install all dependencies

if ["$(UTILITY)" -eq "all"]; then
    for script in ./*.py
    do
        python3 $script $DIR
    done
fi