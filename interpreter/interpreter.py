str = input("Expression:")
operator = ["+","-",'*','/']

stripped = str.split(" ")

x = int(stripped[0])
y = stripped[1]
z = int(stripped[2])

if y == '+':
    print(float(x+z))

elif y == '-':
    print(float(x-z))

elif y == '*':
    print(float(x*z))

elif y == '/':
    print(float(x/z))