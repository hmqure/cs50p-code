from pyfiglet import Figlet

f = "rectangles"
s = "String"

figlet = Figlet()

figlet.getFonts()

figlet.setFont(font=f)

print(figlet.renderText(s))
