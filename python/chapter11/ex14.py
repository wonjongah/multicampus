def test(numbers):
    numbers[0] = -1
    print(numbers)

def test2():
    numbers = [1,2,3]
    return numbers

def main():
    #list1 = [1, 2, 3]
    #test(list1)  # numbers = list1과 같다, 호출하는 값이 대입된다...***************
    #print(list1)
    list2 = test2()   # list2 = numbers와 메커니즘은 같음...
    print(list2)

main()