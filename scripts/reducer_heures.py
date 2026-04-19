#!/usr/bin/env python3
import sys

current_heure = None
total = 0

for line in sys.stdin:
    line = line.strip()
    heure, count = line.split("\t")
    count = int(count)

    if current_heure == heure:
        total += count
    else:
        if current_heure is not None:
            print(current_heure + "h\t" + str(total))
        current_heure = heure
        total = count

if current_heure is not None:
    print(current_heure + "h\t" + str(total))
