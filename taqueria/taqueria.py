dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

counter = 0

while True:
    item = input("Item: ")
    case = item.title()

    try:

        if case in dict:
            counter = counter + dict[case]
            print(f"${counter:.2f}")

        elif case not in dict:
            pass

    except EOFError:

        print(f"${counter:.2f}")
        break

