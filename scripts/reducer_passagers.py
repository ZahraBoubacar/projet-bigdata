#!/usr/bin/env python3
import sys

current_passager = None
total = 0

for line in sys.stdin:
    line = line.strip()
    passager, count = line.split("\t")
    count = int(count)

    if current_passager == passager:
        total += count
    else:
        if current_passager is not None:
            print(str(current_passager) + " passager(s)\t" + str(total) + " trajets")
        current_passager = passager
        total = count

if current_passager is not None:
    print(str(current_passager) + " passager(s)\t" + str(total) + " trajets")
