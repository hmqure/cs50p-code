import inflect

names = []

while True:
    try:
        name = input("Name:")
        names.append(name)

    except EOFError:
        print(join(names))
        break