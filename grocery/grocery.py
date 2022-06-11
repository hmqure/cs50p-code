items = []

while True:
    try:
        item = input("Enter item:")
        lower = item.lower()
        items.append(lower)

    except EOFError:
        pass
        print(items)