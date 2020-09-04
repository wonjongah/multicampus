import os

files = os.listdir('/temp')   # dir /b와 비슷, 그러나 현재 디렉토리의 내용을 리스트로 반환
for f in files:
    print(f)