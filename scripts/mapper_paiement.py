#!/usr/bin/env python3
import sys

modes = {
    "1": "Carte bancaire",
    "2": "Cash",
    "3": "Aucun frais",
    "4": "Litige"
}

for line in sys.stdin:
    line = line.strip()
    if line.startswith("VendorID"):
        continue
    fields = line.split(",")
    if len(fields) != 19:
        continue
    try:
        payment_type = fields[11].strip()
        if payment_type in modes:
            print(modes[payment_type] + "\t" + "1")
    except:
        continue
