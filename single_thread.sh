#!/bin/bash

while :
do
  python3 view.py >> view_log.log || pkill -f chrome
  sleep 10
done
