import sys
from myapp import Application, MenuItem
import MySQLdb


class DBApp(Application):  # 어플리케이션 클래스 정의
    def __init__(self):
        super().__init__()  # 부모 클래스의 생성자 호출
        self.db = MySQLdb.connect(db="sqldb", host="localhost",  # 생성될 때 디비 연결해야겠지~
                                  user="root", passwd="1234", charset='utf8')
        self.cursor = self.db.cursor()  # self 안 쓰면 지역변수 지정임.. 다른데서 못 씀

    def create_menu(self, menu):
        menu.add(MenuItem("목록", self.print_list))
        menu.add(MenuItem("검색", self.search))
        menu.add(MenuItem("추가", self.add))
        menu.add(MenuItem("수정", self.update))
        menu.add(MenuItem("삭제", self.remove))
        menu.add(MenuItem("종료", self.exit))

    def print_list(self):
        try:
            print("목록보기...")

            sql = "SELECT count(*) FROM tblAddr"  # 항상 결과 하나(없으면 0)고, 값도 존재한다! 집계함수니까
            self.cursor.execute(sql)  # if 쓸 필요없음 보장되었음
            row = self.cursor.fetchone()
            total = row[0]
            # 전체 데이터 건수를 추출하는 방법

            sql = "SELECT * FROM tblAddr"  # 읽는 건 커밋 필요 없음!!! 수정하는 제어문엔 커밋필요!!!!!!
            self.cursor.execute(sql)  # 셀렉트의 리턴값음 행의 수!
            rows = self.cursor.fetchall()  # 값 없으면 값 없는 튜플이 된다

            print("===============================")
            print("No  이름     전화번호     주소    ")
            for ix, row in enumerate(rows, 1):
                print(f"{ix} : {row[0]:10} {row[1]:10} {row[2]}")  # 로우 뒤의 :숫자 -> 길이! 열 글자 폭에 맞춰서 출력

            print("===============================")
            print(f"(총 {total} 건)")
        except Exception as e:
            print(e)

    def add(self):
        try:
            print("추가")
            info_name = input("입력할 이름을 입력하세요 : ")
            info_addr = input("입력할 주소를 입력하세요 : ")
            info_phone = input("입력할 전화번호를 입력하세요 : ")

            sql = "INSERT INTO tblAddr VALUES(%s, %s, %s)"
            self.cursor.execute(sql, (info_name, info_phone, info_addr))  # sql 전달할 때 값을 튜플로 전달

            print(f"{info_name}과 {info_phone}과 {info_addr}이 입력되었습니다.")
            self.db.commit()  # 중요!!!!!!! 커밋 안 하면 실제 데베에 적용되지 않는다

        except Exception as e:
            print(e)

    def search(self):
        try:
            print("검색")

            search_name = input("이름 : ")
            sql = f"select count(*) from tblAddr where name like '%{search_name}%'"
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            total = row[0]

            sql = f"select * from tblAddr where name like '%{search_name}%'"
            self.cursor.execute(sql)
            answer = self.cursor.fetchall()

            if not answer:
                print("검색할 이름이 올바르지 않습니다")
                return

            print("="*50)
            header = ("이름", "전화번호", "주소")
            print(f"No  {header[0]:10}{header[1]:10}{header[2]}")
            for ix, row in enumerate(answer, 1):
                print(f"{ix} : {row[0]:10} {row[1]:10} {row[2]}")
            print(f"{search_name}의 내용이 검색됐습니다")
            print("="*50)

        except Exception as e:
            print(e)


    def update(self):
        try:
            print("수정")
            update_name = input("수정할 주소록의 이름을 입력하시오 : ")
            sql = "select * from tblAddr where name = %s"
            self.cursor.execute(sql, (update_name,))
            answer = self.cursor.fetchone()

            if not answer:   # 빈 문자열일 때
                print(f"{update_name} 데이터가 없습니다")
                return

            update_phone = input(f"전화번호({answer[1]}) : ")
            if not update_phone:
                update_phone = answer[1]
            update_addr = input(f"주소({answer[2]}) : ")
            if not update_addr:
                update_addr = answer[2]

            sql = "update tblAddr set phone = %s, addr = %s where name = %s"
            self.cursor.execute(sql, (update_phone, update_addr, update_name))
            self.db.commit()
            print("데이터가 수정되었습니다")

        except Exception as e:
            print(e)

    def remove(self):
        try:
            print("삭제")
            delete_name = input("삭제할 주소록의 이름을 입력하시오 : ")
            sql = "delete from tblAddr where name = %s"
            self.cursor.execute(sql, (delete_name,))
            self.db.commit()

            print(f"{delete_name}을 가진 정보를 삭제했습니다")

        except Exception as e:
            print(e)



    def exit(self):
        yorn = input("종료하시겠습니까 ([y], n)")  # 엔터쳐도 예쓰
        if yorn in ["y", "Y", ""]:  # ""는 엔터만 눌렀을 때
            self.cursor.close()
            self.db.close()
            sys.exit(0)


if __name__ == '__main__':
    app = DBApp()  # 다른데서 부른 게 아니고 여기서 실행된 거면 생성해서 런!
    app.run()  # run()은 부모의 Application의 런!
