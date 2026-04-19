#!/usr/bin/env python3
import sys

current_cat = None
total = 0

for line in sys.stdin:
    line = line.strip()
    categorie, count = line.split("\t")
    count = int(count)

    if current_cat == categorie:
        total += count
    else:
        if current_cat is not None:
            print(current_cat + "\t" + str(total) + " trajets")
        current_cat = categorie
        total = count

if current_cat is not None:
    print(current_cat + "\t" + str(total) + " trajets")
