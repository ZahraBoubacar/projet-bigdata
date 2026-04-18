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
        passenger_count = float(fields[3])
        trip_distance = float(fields[4])
        fare_amount = float(fields[12])
        total_amount = float(fields[18])
        if passenger_count <= 0:
            continue
        if trip_distance <= 0:
            continue
        if fare_amount <= 0:
            continue
        if total_amount <= 0:
            continue
        print(line)
    except:
        continue
