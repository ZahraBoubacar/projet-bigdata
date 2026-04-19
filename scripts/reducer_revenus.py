#!/usr/bin/env python3
import sys

current_heure = None
total = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    heure, montant = line.split("\t")
    montant = float(montant)

    if current_heure == heure:
        total += montant
        count += 1
    else:
        if current_heure is not None:
            moyenne = round(total / count, 2)
            print(current_heure + "h\t" + str(moyenne) + "$")
        current_heure = heure
        total = montant
        count = 1

if current_heure is not None:
    moyenne = round(total / count, 2)
    print(current_heure + "h\t" + str(moyenne) + "$")
