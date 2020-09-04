class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다")


    def __str__(self):   #  현재 내부 정보 리턴해주는 것
        return f"<name:({self.name}), age:({self.age})>"

def main():

        name1 = input("이름을 입력하세요 : ")
        age1 = int(input("나이을 입력하세요 : "))
        won = Human(name1, age1)
        won.intro()
        print(won)
        info = won.__str__()
        print(won)
        won.age = 25   # 인스턴스 변수는 어디서든지 접근 가능
        print(won)


main()