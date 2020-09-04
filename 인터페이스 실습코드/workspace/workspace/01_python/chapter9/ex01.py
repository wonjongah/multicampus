def main():
    nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums = list(range(10))   # 위와 동일
    nums2 = list(range(1,101))   # 1~100까지 리스트 만들기 
    print(nums[:])
    print(nums[2:5])
    print(nums[:4])
    print(nums[6:])
    print(nums[1:7:2])

    print()

    score = [88, 95, 70, 100, 99]
    print(score[2])
    score[2] = 55
    print(score[2])


main()