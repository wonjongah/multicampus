def main():
    dates = ["월", "화", "수", "목", "금", "토", "일"]
    food = ["갈비탕", "순대국", "칼국수", "삼겹살"]
    price = [1, 2, 3, 4]
    menu = zip(dates, food, price)
    for d, f, p in menu:
        print(f"{d}요일 메뉴 : {f}는 {p}원")
        # print("%s요일 메뉴 : %s는 %d원 " % (d, f, p))



main()