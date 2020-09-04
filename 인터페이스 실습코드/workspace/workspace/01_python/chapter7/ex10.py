price = 1000

def sale():
    price = 500
    print("sale", id(price))

sale()
print("global", id(price))