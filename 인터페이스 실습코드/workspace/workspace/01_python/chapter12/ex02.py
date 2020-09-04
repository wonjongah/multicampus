import time
from datetime import datetime  # datetime 모듈의 datetime 함수를 사용하겠다

print(time.time())

t = time.time()
print(time.ctime(t))
print(time.localtime(t))

now = time.localtime()
print(f"{now.tm_year}년{now.tm_mon}월{now.tm_mday}일")
print(f"{now.tm_hour}:{now.tm_min}:{now.tm_sec}")

now = datetime.now()
print(now)
print(f"{now.year}년{now.month}월{now.day}일")
print(f"{now.hour}:{now.minute}:{now.second}")
print()
print(time.strftime("%Y-%m-%d %I:%M"))
timestring = "2019-02-20 12:12:12"
print(time.strptime(timestring, "%Y-%m-%d %I:%M:%S"))
print()
now = datetime.now()
print(time.strftime("%Y-%m-%d %I:%M"))
print()
for i in range(1, 11):    # 이미지 파일 이름...작업...
    fname = now.strftime(f"%Y%m%d%H%M%S-{i:03d}.jpg")
    print(fname)
