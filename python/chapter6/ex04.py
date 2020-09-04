score = [92, 86, 68, 120, 56]
for s in score:
    if(s < 0) or (s > 100):
        print(s, "는 0 미만 혹은 100 초과의 숫자를 입력했습니다. 범위를 벗어났습니다.")
        break
    print(s)
print("성적 처리 끝")

#-----------------------------------------------------------

score = [92, 86, 68, -1, 56]
for s in score:
    if s == -1:
        continue
    print(s)
print("성적 처리 끝")