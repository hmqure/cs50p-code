from tabulate import tabulate
import sys

syst = sys.argv

if len(syst) > 2:
    sys.exit("Too many command-line arguments")

elif len(syst) == 1:
    sys.exit("Too few command-line arguments")

elif len(syst) == 2:
    if (syst[1][-4::]) != ".csv":
        sys.exit("Not a CSV file")

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

                head = splitted[0]
                splitted.pop(0)
                # print(headers)
                # print(splitted)
                print(tabulate(splitted, headers=head, tablefmt="grid"))



        except FileNotFoundError:
            sys.exit("File does not exist")
