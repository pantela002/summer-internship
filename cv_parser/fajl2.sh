#!/bin/bash

nohup python3 c.py -i "$1" -a "$2" -s "$3" -O "$4" > script_output.log 2>&1 &
