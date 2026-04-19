#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if line.startswith("VendorID"):
        continue
    fields = line.split(",")
    if len(fields) != 19:
        continue
    try:
        passenger_count = int(float(fields[3]))
        if passenger_count <= 0:
            continue
        print(str(passenger_count) + "\t" + "1")
    except:
        continue
