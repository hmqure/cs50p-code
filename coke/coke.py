x = 50
print("Amount Due", x)
coins = ['25', '10', '5']

while x != 0:
    coin = input("Insert Coin:")
    if coin in coins:
        x = x - int(coin)
        if x > 0:
            print("Amount Due", x)
        elif x <= 0:
            print("Change Owed:", x*-1)
            break
    else:
        print("Amount Due", x)