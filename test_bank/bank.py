def main():
    str = input("Greeting: ")
    print(value(str))


def value(greeting):
    low = greeting.lower()
    low = low.replace(" ", "")

    if low[0] == "h":
        if low[0:5] == "hello":
            print("$0")
        else:
            print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()