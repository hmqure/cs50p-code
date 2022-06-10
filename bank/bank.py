str = input("Greeting: ")

low = str.lower()
low = low.replace(" ", "")

if low[0] == "h":
    if low[0:5] == "hello":
        print("$0")
    else:
        print("$20")
else:
    print("$100")