class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(str(self.age) + "살" + self.name + "입니다")


class Student(Human):
    def __init__(self, name, age, stunum):  # 메서드 오버라이드 -> 이름도 같고 매개변수도 같아야 한다...
        super().__init__(name, age)  # 부모 클래스의 __init__를 호출, 실행해라!
        self.stunum = stunum  # 추가 정보

    def intro(self):   # 메서드 오버라이드, 덮어썼다! 지워진 건 아님.. 존재함, 재정의 (올라탔다라고 생각)
        super().intro()
        print("학번: " + str(self.stunum))


    def study(self):
        print("하늘천 따지 검을 현 눌를 황")


def main():

    kim = Human("김상형", 29)
    kim.intro()

    lee = Student("이상우", 45, 930011)
    lee.intro()
    lee.study()



main()