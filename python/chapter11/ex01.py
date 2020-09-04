def main():

    race = ["저그", "테란", "프로토스"]
    list(enumerate(race))

    score = [88, 95, 70, 100, 99]
    for no, s in enumerate(score, 1):
        print(str(no) + "번 학생의 성적 : ", s)

main()