def main():
    str = input("Greeting: ")
    print(value(str))


def value(greeting):
    low = greeting.lower()
    low = low.replace(" ", "")

    if low[0] == "h":
        if low[0:5] == "hello":
            return "$0"
        else:
            return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()