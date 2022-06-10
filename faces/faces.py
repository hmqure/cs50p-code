def emojis(str):
        return str.replace(":)", "🙂").replace(":(", "🙁")


string = input("Enter a sentence: ")

print(emojis(string))