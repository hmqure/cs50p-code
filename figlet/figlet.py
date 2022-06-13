from pyfiglet import Figlet
import random
import sys

sys = sys.argv
ok = ['-f', '--font']
figlet = Figlet()
force = figlet.getFonts()


if len(sys) == 3 and sys[1] in ok:
    font1 = sys[2]
    if font1 in force:
        figlet.setFont(font=font1)
        string = input()
        print(figlet.renderText(string))

    else:
        sys.exit("Invalid usage")

elif len(sys) == 1:
    string = input()
    figlet.setFont(font=random.choice(force))
    print(figlet.renderText(string))

else:
    sys.exit("Invalid usage")

