import calendar as cal

dates = ["월", "화", "수", "목", "금", "토", "일"]

day = cal.weekday(2020, 8, 15)
print(f"광복절은 {dates[day]}요일입니다.")