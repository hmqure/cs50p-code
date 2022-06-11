x = 50
print("Amount Due", x)

while x != 0:
    coin = input("Insert Coin:")
    x = x - int(coin)
    if x > 0:
        print("Amount Due", x)
    elif x <= 0:
        print("Change Owed:", x*-1)
        break