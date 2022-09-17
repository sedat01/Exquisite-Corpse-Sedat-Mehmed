setPrice = 10
userPrice = 0
while True:
    userPrice = int(input("Enter price: "))
    if setPrice<userPrice:
        print("It's less")
    elif setPrice>userPrice:
        print("It's more")
    else:
        print("Well done, you won!")
        break
    