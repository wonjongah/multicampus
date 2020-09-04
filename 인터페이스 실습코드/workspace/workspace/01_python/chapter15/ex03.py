import pickle

class UserInfo:
    def __init__(self, name="없음", email="없음", phone="없음"):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"<name : ({self.name}, email : ({self.email}), phone : ({self.phone})>, "

    def __repr__(self):   # 컬렉션에 담겨있는 걸 호출할 때는 이 함수가 호출된다
        return f"<name : ({self.name}>"  # 뭔지만 알면 된다

# 확인을 쉽게 하기 위한 두 가지 메소드 __str__, __repr__ 자세하게 내용 기술해주면 된다

class AddressBook:
    def __init__(self):
        self.book = []   # book 안에 유저의 인스턴스 넣기로
        pass

    def __str__(self):
        pass

    def add(self, name, email, phone):
        ui = UserInfo(name, email, phone)
        self.book.append(ui)

    def find_by_name(self, name):
        for i in self.book:
            if i.name == name:
                return i    # 내가 찾고자하는 이름 없으면 None

    def update(self, name, email, phone):
        ui = self.find_by_name(name)  # 이름이 있는지 없는지
        if not ui:                    # 널인지 아닌지
            print(f"{name}은 목록에 없습니다")
            return
        ui.email = email
        ui.phone = phone

    def remove(self, name):
        ui = self.find_by_name(name)
        if not ui:
            print(f"{name}은 목록에 없습니다")
            return
        self.book.remove(ui)

    def save(self, fpath):
        try:
            with open(fpath, "wb") as f:
                pickle.dump(self.book, f)
        except Exception as e:
            print(e)

    def load(self, fpath):
        try:
            with open(fpath, "rb") as f:
                self.book = pickle.load(f)
        except Exception as e:
            print(e)

    def sort(self, reverse=False):  # 내가 만든 것이기 때문에 파이썬은 비교할 수 없음
        self.book.sort(key=lambda u: u.name, reverse=reverse)  # 이름으로 정렬하라.......

    def search_by_name(self, name):   # 찾은 것들을 리스트에 담아서 리턴하니까 리턴값 리스트
        new_book = []  # 비어있는 리스트 준비하고
        for ui in self.book:  # 시퀀스 순회
            if ui.name.rfind(name) > -1:   # 조건에 맞으면 어펜드로 추가
                new_book.append(ui)
            # if name in ui.name:
        return new_book

    # def search_by_name(self, name):
    # return [ui for ui in self.book if ui.name.fine(name) > -1]


def main():

    """
    user1 = UserInfo("원종아", "wja1511@naver.com", "010-2658-6710")
    print(user1)
    user2 = UserInfo("원종현")
    print(user2)
    l = [
        UserInfo("홍길동", "hong@naver.com", "010-2658-6710"), # 리스트의 첫 번째 요소로 홍길동의 정보 담겠다
        UserInfo("고길동", "go@naver.com", "010-1118-6710")  # 고길동의 참조값이 들어가게 된다
    ] # l = [100, 200]   참조값이 들어간다...

    print(l)

    user1 = UserInfo("홍길동", "hong@naver.com", "010-2658-6710")
    user2 = UserInfo("고길동", "go@naver.com", "010-1118-6710")
    l = [user1, user2]  # 위랑 같다
    # 리스트 프린트할 때는 __str__ 호출되지 않는다... __repr__ 호출된다!
    print(l)
    print(l[0])
    print(user1)

    addr_book = AddressBook()
    addr_book.add("어드레스1", "adrees1", "010-222-3333")
    addr_book.add("어드레스2", "adres2", "010-332-4332")

    print(addr_book.book)

    u1 = addr_book.find_by_name("어드레스1")
    print(u1)
    u2 = addr_book.find_by_name("어드레스3")
    print(u2)
    addr_book.update("어드레스1", "new_adrress1", "01010101010")
    u1 = addr_book.find_by_name("어드레스1")
    print(u1)
    addr_book.update("어드레스3", "new_address3", "01020202020")

    print()

    addr_book.remove("어드레스1")
    u1 = addr_book.find_by_name("어드레스")
    print(u1)

    print()

    users = addr_book.search_by_name("어드")
    print(users)
    users = addr_book.search_by_name("2")
    print(users)
    users = addr_book.search_by_name("어드레스1")
    print(users)

    file_name = "book1.dat"
    addr_book = AddressBook()

    addr_book.add("홍길동", "hong@", "01022223333")
    addr_book.add("고길동", "go@", "01011112222")
    addr_book.save(file_name)

    addr_book2 = AddressBook()
    addr_book2.load(file_name)
    print(addr_book2.book)

    """
    file_name = "book1.dat"
    addr_book = AddressBook()

    addr_book.load(file_name)
    print(len(addr_book.book))  # 몇 개의 항목이 있나~~~~

    addr_book.sort()
    print(addr_book.book)
"""
    for ix in range(1, 100):
        if ix % 2 == 0:
            addr_book.add(f"홍길동{ix}", f"hong{ix}@", "010-1111-1111")
        else:
            addr_book.add(f"고길동{ix}", f"go{ix}@", "010-2222-2222")
    addr_book.save(file_name)
    """

main()


