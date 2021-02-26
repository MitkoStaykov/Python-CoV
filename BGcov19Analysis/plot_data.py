#!/usr/bin/env python
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages = list()
life_exp = 74.82

with open("all_raw_numbers(4).txt", mode="r") as f:
    for line in f:
        ages = line.split(',')

print (len(ages))
ages = [int(i) for i in ages] 

n = len(ages)
s = 0

for el in ages:
    s+=int(el)
med = s/n

bins = range(5,105,1)
#bins = [20,40,60,80,100]
plt.hist(ages, bins=bins)
plt.axvline(life_exp, color='#fcff10', label='LIFE EXP', linewidth=2)
plt.axvline(med, color='#2c4ffc', label='MEAN UNTIL NOW', linewidth=2)
plt.legend()
plt.show()