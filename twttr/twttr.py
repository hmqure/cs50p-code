enter = input("Input:")

new = ''
vowels = ["A", 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for i in range(len(enter)):
    if enter[i] not in vowels:
        new += enter[i]

print(new)