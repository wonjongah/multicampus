import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees',   # use employees와 같은 표현
                     user='root', passwd='1234')    # 유저아이디 패스워드
# 올바르면 객체가 db 객체가 생성됐다
# db는 세션을 관리
cursor = db.cursor()   # sql 문장 실행하려면 필요한 커서
# cursor는 sql 문장을 관리
print("접속에 성공했습니다.")


sql = """SELECT * FROM EMPLOYEES 
ORDER BY HIRE_DATE DESC 
LIMIT 10""" #가장 최근에 입사한 순서로 열명

cursor.execute(sql)   # sql 담긴 변수를 매개변수로 전달하면, 실행해준다!

rows = cursor.fetchall()  # fetchall은 다 가져오는 것!
for row in rows:
    print(row)


cursor.close()
db.close()