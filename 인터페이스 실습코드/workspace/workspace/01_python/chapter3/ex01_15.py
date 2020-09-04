score = int(input("점수 : "))
if score < 60:
    print(score, 'F')
elif score < 70:
    print(score, 'D')
elif score < 80:
    print(score, 'C')
elif score < 90:
    print(score, 'B')
else:
    print(score, 'A')