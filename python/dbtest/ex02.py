import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees',
                     user='root', passwd='1234')

cursor = db.cursor()



sql = """
"""

cursor.execute(sql)

# 필요한 작업 실행

cursor.close()
db.close()