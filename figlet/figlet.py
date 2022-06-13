from pyfiglet import Figlet
import random
import sys
f = input()
s = "String"

try:
    if f != "":
        split = f.split(" ")
        if split[0] == "-f" or split[0] == "--font":
            font1 = split[1]

    elif f == "":
        string = input()
        figlet.setFont(random.)
        print(figlet.renderText(string))



    figlet = Figlet()
    figlet.getFonts()

    figlet.setFont(font=f)

    print(figlet.renderText(s))
