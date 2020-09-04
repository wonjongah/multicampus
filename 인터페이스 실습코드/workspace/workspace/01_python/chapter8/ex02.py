s = "python"
print(s[2])
print(s[-2])

for c in s:
    print(c, end=",")
print()
for i in range(len(s)):  # 글자의 수만큼 루프를 돌아라
    print(s[i], end=",") # i는 0부터 5까지, 즉 인덱스로 사용
print()
s = "0123456789"
print(s[2:5])
print(s[3:])
print(s[:4])

print()

file = "20200101-104830.jpg"
print("촬영날짜" + file[4:6] + "월" + file[6:8] + "일")
print("촬영시간" + file[9:11] + "시" + file[11:13] + "분")
print("확장자" + file[-3:])

dates = "월화수목금토일"
print(dates[::2])
print(dates[::-1])