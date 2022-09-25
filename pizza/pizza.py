import tabulate
import sys

if len(syst) > 2:
    sys.exit("Too many command-line arguments")

elif len(syst) == 1:
    sys.exit("Too few command-line arguments")

elif len(syst) == 2:
    if (syst[1][-3::]) != ".py":
        sys.exit("Not a python file")

    else:
        try:
            with open(syst[1], "r") as file:
                line = file.readlines()
                line_list.append(line)

                for i in line_list[0]:
                    if not i.lstrip().startswith('#') and i.lstrip() != '':
                        fin_list.append(i)

        except FileNotFoundError:
            sys.exit("File does not exist")


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

headers = splitted[0]
print(headers)

# print(tabulate.grid('sicilian.csv'))

# print(tabulate(mydata, headers=head, tablefmt="grid"))