from tabulate import tabulate
import sys
import csv

syst = ['1.pn', 'dsdg.pol']
extensions = ['jpg','jpeg','png']

sysext = []


for i in syst:
    sysext.append(i.split(".")[1])

if sysext[0] not in extensions:
    print("no")

print(sysext)