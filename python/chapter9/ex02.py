def main():
    nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums = list(range(10))

    nums2 = nums
    print(nums == nums2)
    nums[0] = -1
    nums2[2] = -2
    print(nums)
    print(nums2)
    print(nums == nums2)

    nums = list(range(10))
    nums2 = list(range(10))
    print(nums == nums2)   # 변수는 두 개지만 실 데이터는 한 개로

main()