#!/usr/bin/env python3
import sys

current_mode = None
total = 0

for line in sys.stdin:
    line = line.strip()
    mode, count = line.split("\t")
    count = int(count)

    if current_mode == mode:
        total += count
    else:
        if current_mode is not None:
            print(current_mode + "\t" + str(total) + " trajets")
        current_mode = mode
        total = count

if current_mode is not None:
    print(current_mode + "\t" + str(total) + " trajets")
