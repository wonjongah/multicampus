student = 1
while student <= 5:  # : => while문에 종속되는 코드블럭이 나온다
    print(student, "번 학생의 성적을 처리합니다")
    student += 1
# ----------------------------------------------------------
num = 1
total = 0
while num <= 100:
    total += num
    num += 1
print("total = ", total)
# ----------------------------------------------------------
num = 2
total = 0
while num <= 100:
    total += num
    num += 2
print("total = ", total)
# 짝수의 합
# ---------------------------------------------------------
num = 1
totalodd = 0
totaleven = 0

while num <= 100:
    if num % 2 == 0:
        totaleven += num
    else:
        totalodd += num
    num += 1

print("짝수의 합은 ", totaleven)
print("홀수의 합은 ", totalodd)