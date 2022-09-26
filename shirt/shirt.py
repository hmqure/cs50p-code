from PIL import Image
import sys


syst = sys.argv
extensions = ['jpg','jpeg','png']

sysext = []

for i in syst:
    sysext.append(i.split(".")[1])

if len(syst) > 3:
    sys.exit("Too many command-line arguments")

elif len(syst) <= 2:
    sys.exit("Too few command-line arguments")

elif len(syst) == 3:
    if sysext[1].lower() not in extensions:
        sys.exit('Invalid input')

    elif sysext[2].lower() not in extensions:
        sys.exit('Invalid input')

    elif sysext[1].lower() != sysext[2].lower():
        sys.exit('Input and output have different extensions')

    else:
        try:
            print(syst[1])


            # with open(syst[1], "r") as file:
            #     menu = file.readlines()

            #     stripped = []

            #     for items in menu:
            #         strip = (items.strip('\n'))
            #         stripped.append(strip)#.split('\t'))

            #     splitted = []

            #     for i in stripped:
            #         splitted.append(i.split(','))

            #     splitted.pop(0)

            #     first = []
            #     last = []
            #     house = []

            #     for i in splitted:
            #         first.append(i[1].replace('"', '').replace(' ',''))
            #         last.append(i[0].replace('"', ''))
            #         house.append(i[2])

            #     with open(syst[2], 'w') as after:
            #         writer = csv.writer(after)

            #         header = ['first','last','house']

            #         writer.writerow(header)

            #         data = []

            #         for i in range(len(first)):
            #             data.append([first[i], last[i], house[i]])

            #         for i in data:
            #             writer.writerow(i)

            #         after.close()

        except FileNotFoundError:
            sys.exit("File does not exist")
