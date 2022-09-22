import sys

syst = sys.argv

line_list = []

if len(syst) > 2:
    sys.exit("Too many command-line arguments")

elif len(syst) == 1:
    sys.exit("Too few command-line arguments")

elif len(syst) == 2:
    if (syst[1][-3::]) != ".py":
        sys.exit("Not a python file")

    else:
        with open(syst[1], "r") as file:
            line = file.readlines()
            for i in line:
                print(i)
                
                #if i[0] != "#" or i[0] != '\n':
                    #line_list.append(line)
                    #print(line_list)
                    #print(len(line_list[0]))

# not found
# exclude white spaces and comments