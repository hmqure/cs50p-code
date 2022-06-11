camel = input("camelCase:")

capital = []
new = ''

for i in range(len(camel)):
    if camel[i].isupper() is True:
        capital.append(camel[i])

for i in camel:
    if i not in capital:
        new += i
    elif i in capital:
        new += ("_"+i)

print(new.lower())