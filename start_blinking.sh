#!/bin/bash
NOW="$(date '+%Y %m %d %H:%M:%S')"
NOW_LOG="_$(date '+%Y-%m-%d')"
workpath="/home/pi/blink-lights"
process_execution="main.py"
process_name="blink-lights"


echo "initializing $process_name at: $NOW"
python $process_execution --on 19 --of 22
