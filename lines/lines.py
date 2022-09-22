import sys

syst = sys.argv

line_list = []
fin_list = []

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
                if i[0] != '#':
                    if i[0] != '\n':
                        fin_list.append(i)




print(len(fin_list))



            #print(len(line_list[0]))

# not found
# exclude white spaces and comments