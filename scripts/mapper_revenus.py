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
        heure = fields[1].split(" ")[1].split(":")[0]
        total_amount = float(fields[18])
        if total_amount <= 0:
            continue
        print(heure + "\t" + str(total_amount))
    except:
        continue
