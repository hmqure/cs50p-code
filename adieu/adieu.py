import inflect

names = []
p = inflect.engine()

while True:
    try:
        name = input("Name:")
        names.append(name)

    except EOFError:
        print(p.join(names, final_sep=","))
        break