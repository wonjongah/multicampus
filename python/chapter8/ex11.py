def main():

    mont = 8
    day = 15
    anni = "광복절"
    print("%d월 %d일은 %s이다." % (mont, day, anni))

    price = [30, 13500, 2000]
    for p in price:
        print("가격 : %d원"%p)
    for p in price:
        print("가격 : %7d원"%p)
    for p in price:
        print("가격 : %-7d원"%p)


main()