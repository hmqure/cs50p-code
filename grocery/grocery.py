items = []

while True:
    try:
        item = input()
        lower = item.lower()
        items.append(lower)

    except EOFError:
        pass
        print(items)