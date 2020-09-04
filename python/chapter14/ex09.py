try:
     with open('live.txt', 'r') as file:
     text = file.read()
     print(text)
except FileNotFoundError:
     print("파일이 없습니다.")