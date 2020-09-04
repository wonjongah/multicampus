class Addr:  # 정보보관용, 데이터 클래스, 튜플 대신!! 가독성 높여줄 수 있다
# 가독성을 높이기 위해서 튜플로 관리하던 것을 모델클래스로 관리하겠다
# 이 모델클래스 정의가 테이블을 말하고 있다
# 이 필드들.... 컬럼 역할을 하고 있음
# 클래스 정의가 테이블 정의와 같다.......
# 실제 테이블 한 행은 해당 모델 클래스의 인스턴스.....와 맵핑

    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr

    def __str__(self):
        return f"<Addr {self.name}/{self.phone}/{self.addr}>"

    def __repr__(self):
        return f"<Addr {self.name}>"