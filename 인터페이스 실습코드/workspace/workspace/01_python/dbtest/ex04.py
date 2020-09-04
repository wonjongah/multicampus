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

cursor.execute("SELECT addr, phone FROM tblAddr WHERE name = '김상형'")

record = cursor.fetchone()
print(record)
if record : print(f"김상형은 {record[0]}에 살고, {record[1]}의 전화번호를 가지고 있습니다")
else: print("김상형은 없는 이름입니다")

db.commit()
# 필요한 작업 실행

cursor.close()
db.close()