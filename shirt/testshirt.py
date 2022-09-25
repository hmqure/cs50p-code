from tabulate import tabulate
import sys
import csv

syst = ['lines.py','1.jpg', 'dsdg.jpg']
extensions = ['jpg','jpeg','png']

sysext = []


for i in syst:
    sysext.append(i.split(".")[1])

if sysext[1] not in extensions:
    print("no")
else:
    print('yes')

print(sysext)