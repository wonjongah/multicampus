def main():

    s = "짜장 짬뽕 탕수육"
    print(s.split())

    s2 = "서울->대전->대구->부산"
    cities = s2.split("->")
    print(cities)

    for city in cities:
        print(city)

main()