#!/bin/sh
cd /
cd home/pi/stream-listener/
nohup python3 main.py >/dev/null 2>&1 &
cd /
