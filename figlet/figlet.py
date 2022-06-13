from pyfiglet import Figlet
import random
import sys
sys = sys.argv

figlet = Figlet()
force = figlet.getFonts()


try:

    if len(sys) == 3:
        arg = sys[1]
        font1 = sys[2]

    elif len(sys) == 1:

except EOFError as e:
    print(e)

#     if f != "":
#         split = f.split(" ")
#         if split[0] == "-f" or split[0] == "--font":
#             string = input()
#             font1 = split[1]
#             if font1 in force:
#                 figlet.setFont(font=font1)
#                 print(figlet.renderText(string))

#             else:
#                 sys.exit("Invalid usage")

#         else:
#             sys.exit("Invalid usage")

#     elif f == "":
#         string = input()
#         figlet.setFont(font=random.choice(force))
#         print(figlet.renderText(string))

# except EOFError as e:
#     print(e)

    # elif f == "":
    #     string = input()
    #     figlet.setFont(random.)
    #     print(figlet.renderText(string))



    # figlet = Figlet()
    # figlet.getFonts()

    # figlet.setFont(font=f)

    # print(figlet.renderText(s))
