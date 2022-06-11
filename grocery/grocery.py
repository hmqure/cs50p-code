items = []
finals = []
ff = []

while True:
    try:

        item = input()
        upper = item.upper()
        items.append(upper)

    except EOFError:

        for i in items:
            finals.append(f'{items.count(i)} {i}')

        for i in finals:
            if i not in ff:
                ff.append(i)

        for i in ff:
            print(i)

        break

