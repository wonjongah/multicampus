def main():
    list1 = [1, 2, 3]
    list2 = list1   # 복사본 없다
    print(list1 == list2)
    list2[1] = 100
    print(list1)
    print(list2)
    print(list1 == list2)


main()