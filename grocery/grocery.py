items = []
finals = []
ff = []

while True:
    try:

        item = input("Enter item:")
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

        for i in ff:
            print(i)
