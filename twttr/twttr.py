
enter = input("Input:")

new = ''
vowels = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']

for i in range(len(enter)):
    if enter[i] not in vowels:
        new += enter[i]

print(new)



