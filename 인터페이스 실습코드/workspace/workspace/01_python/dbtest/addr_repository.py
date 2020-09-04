from addr_models import Addr


class AddressRepository:  # 유지보수 위해 리팩토링, 여기는 데베
    
    def __init__(self, db):
        self.cursor = db.cursor()
        # 어플리케이션은 이제 커서 객체를 관리하지 않는다.. DB만 관리한다 어플리케이션에서는
        
    def close(self):
        self.cursor.close()
        
    def get_total(self, where=''):    # 데이터건수 구하는 메서드
        sql = "SELECT count(*) FROM tblAddr " + where  # 항상 결과 하나(없으면 0)고, 값도 존재한다! 집계함수니까
        self.cursor.execute(sql)  # if 쓸 필요없음 보장되었음
        row = self.cursor.fetchone()
        return row[0]


    def get_list(self, where=''):
        sql = "SELECT * FROM tblAddr " + where  # 읽는 건 커밋 필요 없음!!! 수정하는 제어문엔 커밋필요!!!!!!
        self.cursor.execute(sql)  # 셀렉트의 리턴값음 행의 수!
        rows= self.cursor.fetchall()  # 값 없으면 값 없는 튜플이 된다
        # return rows
        return (Addr(*row) for row in rows)
    def insert(self, data):
        sql = "INSERT INTO tblAddr VALUES(%s, %s, %s)"
        self.cursor.execute(sql, (data.name, data.phone, data.addr))  # sql 전달할 때 값을 튜플로 전달


    def remove(self, name):
        sql = "delete from tblAddr where name = %s"
        self.cursor.execute(sql, (name,))  # (name, ) -> 데이터가 한 개라는 걸 알려줌


    def get_one(self, name):
        sql = "select * from tblAddr where name = %s"
        self.cursor.execute(sql, (name,))
        row = self.cursor.fetchone()
     #  addr = Addr(*row)   # 튜플 위치기반으로  **는 딕셔너리
      # return addr  # addr은 튜플이 아님, 어드레스 모델 객체!
        if row:
            return Addr(*row) #* 위치기반의 인자로 펼쳐서 전달한다
    def update(self, data):
        sql = f"update tblAddr set phone = %s, addr = %s where name = %s"
        self.cursor.execute(sql, (data.phone, data.addr, data.name))