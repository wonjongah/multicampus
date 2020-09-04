def main():

    nums = list(range(1, 10))
    nums[2:5] = [20,30,40]    # 이전값 삭제하고 추가
    print(nums)
    nums[6:6] = [1000, 2000]  # 이전값 삭제하지 않고 추가
    print(nums)

    nums[6:8] = [60,70,80,90]
    print(nums)


    str1 = "hello"
    str2 = "world"
    str3 = str1 + str2

    print(str3)

    str4 = str1 * 3

    print(str4)
main()