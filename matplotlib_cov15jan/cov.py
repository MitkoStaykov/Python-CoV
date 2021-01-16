from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages = list()
life_exp = 74.82
with open("cov.txt",encoding="utf-8", mode="r") as f:
    for line in f:
        a = line.split()
        if len(a)>1:
            ages.append(int(a[2]))
#print (ages)
n = len(ages)
s = 0
for el in ages:
    s+=el
#print (s/n)
med = s/n
bins = [50,55,60,65,70,75,80,85,90]
plt.hist(ages, bins=bins)
plt.axvline(life_exp, color='#fc4f30', label='LIFE EXP', linewidth=2)
plt.axvline(med, color='#2c4ffc', label='MEAN 15.JAN.2021', linewidth=2)
plt.legend()
plt.show()