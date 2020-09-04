import sys
from myapp import Application, MenuItem
import MySQLdb
from addr_repository import AddressRepository
from addr_ui import *   # 모듈함수 다 임포트하겠다
import sqlite3   # 파이썬의 표준모듈

# ----------------------sqlite3로 바꿀 것----호환 가능-----


class DBApp(Application):  # 어플리케이션 클래스 정의
    def __init__(self):
        super().__init__()  # 부모 클래스의 생성자 호출
        """self.db = MySQLdb.connect(db="sqldb", host="localhost",  # 생성될 때 디비 연결해야겠지~
                                  user="root", passwd="1234", charset='utf8')"""
        self.db = sqlite3.connect("c:/temp/text.db")
        self.repo = AddressRepository(self.db)  # repo 생성, 커서대신!!!!!!

    def create_menu(self, menu):
        menu.add(MenuItem("목록", self.print_list))
        menu.add(MenuItem("검색", self.search))
        menu.add(MenuItem("추가", self.add))
        menu.add(MenuItem("수정", self.update))
        menu.add(MenuItem("삭제", self.remove))
        menu.add(MenuItem("종료", self.exit))

    def print_list(self):

        print("목록보기...")

        total = self.repo.get_total()   # 세부기능은 하위모듈, 어플리케이션은 순서 즉 흐름제어만 신경씀
        rows = self.repo.get_list()
        print_list(total, rows)



    def add(self):

        print("추가")
        add_info = input_addr_info()

        self.repo.insert(add_info)

        print(f"{add_info[0]}과 {add_info[1]}과 {add_info[2]}이 입력되었습니다.")
        self.db.commit()  # 중요!!!!!!! 커밋 안 하면 실제 데베에 적용되지 않는다



    def search(self):

        print("검색")

        search_name = input("이름 : ")
        where = f"where name like '%{search_name}%'"
        total = self.repo.get_total(where)
        rows = self.repo.get_list(where)

        print_list(total, rows)




    def update(self):

        print("수정")
        update_name = input("수정할 주소록의 이름을 입력하시오 : ")
        answer = self.repo.get_one(update_name)

        if not answer:
            print("일치하는 데이터가 없습니다")
            return

        data = input_addr_info(update_name)
        self.repo.update(data)
        self.db.commit()
        print("데이터가 수정되었습니다")



    def remove(self):

        print("삭제")
        delete_name = input("삭제할 주소록의 이름을 입력하시오 : ")
        self.repo.remove(delete_name)
        self.db.commit()   # 커서의 메서드가 아니고 디비 객체의 것, 한꺼번에 커밋하는 게 좋음

        print(f"{delete_name}을 가진 정보를 삭제했습니다")



    def exit(self):
        yorn = input("종료하시겠습니까 ([y], n)")  # 엔터쳐도 예쓰
        if yorn in ["y", "Y", ""]:  # ""는 엔터만 눌렀을 때
            self.repo.close()
            self.db.close()
            sys.exit(0)


if __name__ == '__main__':
    app = DBApp()  # 다른데서 부른 게 아니고 여기서 실행된 거면 생성해서 런!
    app.run()  # run()은 부모의 Application의 런!

