"""
print("3 + 4 = ?")
num = 0
while True:
    a = int(input("정답을 입력하세요:"))
    if a == 7 : break
    else:
        num += 1
        if num > 2:
            print("3번을 초과했습니다")
            break

print("참 잘했어요")
"""

result = False
print("3 + 4 = ?")
for num in range(3):
    a = int(input("정답을 입력하세요"))
    if a == 7:
        result = True  # 정답이 맞았을 경우, 로그인에서 주로 쓰임
        break
if result:
    print("참 잘했어요")
else:
    print("실패했습니다")
