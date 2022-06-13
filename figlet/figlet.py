from pyfiglet import Figlet

f = input()
s = "String"

figlet = Figlet()

figlet.getFonts()

figlet.setFont(font=f)

print(figlet.renderText(s))
