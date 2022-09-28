from random import choice as pasirinkimas

pasrinkimai = ["Vienas", "du", "trys", "keturi", "penki"]
for chance in range(10):
    # pasirinktas = random.choice(pasrinkimai)
    # pasirinktas = choice(pasrinkimai)
    pasirinktas = pasirinkimas(pasrinkimai)
    print(pasirinktas)

print("-----------------------")
print("-----------------------")
print("-----------------------")

from datetime import datetime as dt
print(dt.now()) #dabartinis laikas!!!

print("___________________")
print("___________________")
print("___________________")

from calendar import isleap
for metai in range(0, 2400, 100):
    print(metai, isleap(metai))
    print("*******")

print("--------------")
print("--------------")
print("--------------")

import os
print(os.getcwd()) # suzinome dabartine direktorija

print("---------------------")
print("---------------------")
print("---------------------")

from math import sqrt
for skaicius in range(20):
    print(sqrt(skaicius))
    print("**")

print("-----------------")
print("-----------------")
print("-----------------")

