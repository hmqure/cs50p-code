from tabulate import tabulate
import sys
import csv

syst = sys.argv

if len(syst) > 3:
    sys.exit("Too many command-line arguments")

elif len(syst) <= 2:
    sys.exit("Too few command-line arguments")

elif len(syst) == 3:
    if (syst[1][-4::]) != ".csv":
        sys.exit("Could not read", syst[1])

    elif (syst[2][-4::]) != ".csv":
        sys.exit("Could not read", syst[2])

    else:
        try:
            with open(syst[1], "r") as file:
                menu = file.readlines()

                stripped = []

                for items in menu:
                    strip = (items.strip('\n'))
                    stripped.append(strip)#.split('\t'))

                splitted = []

                for i in stripped:
                    splitted.append(i.split(','))

                splitted.pop(0)

                first = []
                last = []
                house = []

                for i in splitted:
                    first.append(i[1].replace('"', '').replace(' ',''))
                    last.append(i[0].replace('"', ''))
                    house.append(i[2])

                with open(syst[2], 'w') as after:

                    


        except FileNotFoundError:
            sys.exit("File does not exist")
