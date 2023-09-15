#!/bin/bash

nohup python3 c.py -i "$1" -a "$2" > script_output.log 2>&1 &
