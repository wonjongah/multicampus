import MySQLdb

db = MySQLdb.connect(db="sqldb", host="localhost",
 user="root", passwd="1234", charset='utf8')   # 데베 꺼져있으면 커넥션에서 에러.. 여기도 예외처리

cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS tblAddr')

cursor.execute("""
CREATE TABLE tblAddr(
 name CHAR(16) PRIMARY KEY,
 phone CHAR(16),
 addr TEXT
)
""")
try:  # input할 때 예외 가장 많이 일어남, Duplicate entry '김상형' for key 'PRIMARY' -> 기본키 중복 입력하려고 할 때
    # data too long 정한 데이터 길이보다 길 때
    names = input("입력할 이름을 입력하세요 : ")
    phones = input("입력할 전화번호를 입력하세요 : ")
    addrs = input("입력할 주소를 입력하세요 : ")

    cursor.execute(f"INSERT INTO tblAddr VALUES('{names}', '{phones}', '{addrs}')")
    # sql = "INSERT INTO tblAddr VALUES(%s, %s, %s)"
    # cursor.execute(sql, (names, phones, addr))
    # db.commit()

    cursor.execute("INSERT INTO tblAddr VALUES('김상형', '123-4567', '오산')")
    cursor.execute("INSERT INTO tblAddr VALUES('한경은', '555-1004', '수원')")
    cursor.execute("INSERT INTO tblAddr VALUES('한주완', '444-1092', '대전')")

    name = input("검색할 이름을 입력하세요 : ")
    # cursor.execute(f"SELECT addr, phone FROM tblAddr WHERE name = '{name}'")

    sql = "SELECT name, addr, phone FROM tblAddr WHERE name = %s"
    cursor.execute(sql, (name,))
    record = cursor.fetchone()
    print(record)
    if record : print(f"{record[0]}은 {record[1]}에 살고, {record[2]}의 전화번호를 가지고 있습니다")
    else: print("없는 이름입니다")

    cursor.execute("UPDATE tblAddr SET addr = '제주도' WHERE name = '김상형'")
    cursor.execute("DELETE from tblAddr where name = '한경은'")
    cursor.execute("SELECT * FROM tblAddr ORDER BY addr")

    rows = cursor.fetchall()  # fetchall은 다 가져오는 것!
    for row in rows:
        print(row)

    db.commit()
    # 필요한 작업 실행
except Exception as e:
    print(e)

cursor.close()
db.close()