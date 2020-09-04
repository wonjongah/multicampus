def findMin(*ints):
    minin = 1000000     # 범용함수가 되기 위해서, 튜플의 첫 번째 요소와 두 번째 요소부터 루프 돌리면서 비교
    for i in ints:
        if i < minin:    # 새로운 최소값이 발견됐으면 변경
            minin = i
    return minin

def findMax(*ints):
    maxin = -1111111
    for i in ints:
        if i > maxin:
            maxin = i
    return maxin



maxout = findMax(3,23, 15, -1, 100, 1000)
minout = findMin(2, 7, 5, -1, 20)
print("최소값: ", minout)
print("최대값: ", maxout)