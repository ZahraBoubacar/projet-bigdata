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
        pickup_datetime = fields[1]
        heure = pickup_datetime.split(" ")[1].split(":")[0]
        print(heure + "\t" + "1")
    except:
        continue
