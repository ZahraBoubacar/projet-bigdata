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
        distance = float(fields[4])
        if distance <= 0:
            continue
        if distance <= 1:
            categorie = "0-1 miles"
        elif distance <= 5:
            categorie = "1-5 miles"
        elif distance <= 10:
            categorie = "5-10 miles"
        else:
            categorie = "+10 miles"
        print(categorie + "\t" + "1")
    except:
        continue
