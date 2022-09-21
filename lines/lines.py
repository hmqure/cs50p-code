import sys

sys = sys.argv

line_list = []

if len(sys) > 2:
    print("Too many command-line arguments")

elif len(sys) == 1:
    print("Too few command-line arguments")

elif len(sys) == 2:
    if (sys[1][-3::]) != ".py":
        print("Not a python file")

    else:
        with open(sys[1], "r") as file:
            line = file.readlines()
            line_list.append(line)
            print(len(line_list[0]))
