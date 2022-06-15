
enter = input("Input:")

new = ''
vowels = ['a', 'e', 'i', 'o', 'u']

lower = word.lower()

for i in range(len(lower)):
    if lower[i] not in vowels:
        new += lower[i]

print(new)



