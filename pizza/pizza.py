import tabulate

file = 'sicilian.csv'

with open(file, 'r') as file:        #open tab file
    menu = file.readlines()

stripped = []

for items in menu:
    strip = (items.strip('\n'))
    stripped.append(strip)#.split('\t'))

splitted = []

for i in stripped:
    splitted.append(i.split(','))

print(splitted)

print(tabulate.grid('sicilian.csv'))

print(tabulate(mydata, headers=head, tablefmt="grid"))