items = []

while True:
    try:
        item = input("Enter item:")
        lower = item.lower()
        items.append(lower)

    except EOFError:
        for i in items:
            print(i.count())