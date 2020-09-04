import MySQLdb

db = MySQLdb.connect(db="sqldb", host="localhost",
 user="root", passwd="1234", charset='utf8')

cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS tblAddr')

cursor.execute("""
CREATE TABLE tblAddr(
 name CHAR(16) PRIMARY KEY,
 phone CHAR(16),
 addr TEXT
)
""")

cursor.execute("INSERT INTO tblAddr VALUES('김상형', '123-4567', '오산')")
cursor.execute("INSERT INTO tblAddr VALUES('한경은', '555-1004', '수원')")
cursor.execute("INSERT INTO tblAddr VALUES('한주완', '444-1092', '대전')")

cursor.execute("SELECT * FROM tblAddr ORDER BY addr")

table = cursor.fetchall()  # where 절 없는 select는 보통 fetchall() 쓴다
# fetchone() => 프라이머리키일때...
print(type(table), table)

for record in table:
 print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")

db.commit()
# 필요한 작업 실행

cursor.close()
db.close()