from pyfiglet import Figlet
import random
import sys
f = input()
s = "String"

figlet = Figlet()
figlet.getFonts()
# figlet.setFont(font=f)
# print(figlet.renderText(s))

try:
    if f != "":
        split = f.split(" ")
        if split[0] == "-f" or split[0] == "--font":
            string = input()
            font1 = split[1]
            figlet.setFont(font=font1)
            print(figlet.renderText(string))

    elif f == "":
        string = input()
        figlet.setFont(random.)
        print(figlet.renderText(string))

except EOFError as e:
    print(e)

    # elif f == "":
    #     string = input()
    #     figlet.setFont(random.)
    #     print(figlet.renderText(string))



    # figlet = Figlet()
    # figlet.getFonts()

    # figlet.setFont(font=f)

    # print(figlet.renderText(s))
