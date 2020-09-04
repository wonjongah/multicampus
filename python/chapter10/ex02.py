def main():

    print(set("aaabbbccc"))
    print(set([12, 34, 56, 78]))
    print(set(("홍길동", "고길동","둘리")))
    print(set({"boy": "소년", "school": "학교", "book": "책"}))
    print(set())


    asia = {"korea", "china", "japan"}
    asia.add("vietnam")
    asia.add("korea")
    asia.remove("japan")
    print(asia)


main()