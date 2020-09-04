message = "안녕하세요"
print(message.ljust(30))
print(message.center(30))
print(message.rjust(30))

list1 = [1,5,10, 8, 3]
print(sorted(list1))
print(list1)
list1.sort()
print(list1)

name = "이순신", "김유신", "강감찬"
lee, kim, kang = name
print(lee)
print(kim)
print(kang)

dic = {'boy': '소년', 'school': '학교', 'book': '책'}
dic['boy'] = '남자아이'  # 기존값 수정
dic['girl'] = '소녀'  # 새로운 엔트리 추가

del dic['book']  # 기존 엔트리 삭제

print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

dic = { 'boy': '소년', 'school': '학교', 'book':'책'}
dic2 = { 'student': '학생', 'teacher': '선생님', 'book':'서적'}
dic.update(dic2)
print(dic)

asia = {'korea', 'china', 'japan'}
asia.add('vietnam')
asia.add('korea')
asia.remove('japan')
print(asia)


def flunk(s):
    return s < 60
score = [45, 89, 72, 53, 94]
print(filter(flunk, score))

list1 = [1, 2, 3]
list2 = list1
print(list1 == list2)
list2[1] = 100
print(list1)
print(list2)
print(list1 == list2)

list1 = [1, 2, 3]
list2 = list1.copy() # list2 = list1[:]와 동일
print(list1 == list2)
list2[1] = 100
print(list1)
print(list2)
print(list1 == list2)

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def intro(self):
        print(self.name + str(self.age))

class Student(Human):
    def __init__(self, age, name):
        super().__init__(age, name)
    def haha(self):
        print('haha' + self.name)

s1 = Student(13, '김경화')
s1.haha()
h1 = Human(23, 'dd')
h1.intro()
s1.intro()

