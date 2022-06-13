import inflect

names = []

while True:
    try:
        name = input("Name:")
        names.append(name)

    except EOFError:
        print(p.join(names))
        break