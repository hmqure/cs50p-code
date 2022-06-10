str = input("what is the meaning of life?")

low = str.lower()
low = low.replace("-", " ")
low = low.replace(" ", "")

if low == "42" or low == "fortytwo":
    print("Yes")
else:
    print("No")