man1 = input("성별을 입력하시오")
if man1 == "남자":
    man = True
else:
    man = False

age = int(input("나이를 입력하시오"))

if man == True:
    if age > 19:
        print("성인 남자입니다")
    else:
        print("미성년 남자입니다")
else:
    if age > 19:
        print("성인 여자입니다")
    else:
        print("미성년 여자입니다")