from pyfiglet import Figlet
import random
import sys
f = input()
s = "String"

try:
    if f != "":
        split = f.split(" ")
        if split[0] == "-f" or split[0] == "--font":
            font = split[1]

    elif f == "":
        string = input()



    figlet = Figlet()
    figlet.getFonts()

    figlet.setFont(font=f)

    print(figlet.renderText(s))
