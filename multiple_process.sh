#!/bin/bash

for i in {1..5};
  do python3 view.py >> view_log.log &
done
wait


