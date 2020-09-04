import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = os.path.join(path, f)   # 패스와 패스 결합할 때 주로 사용, 운영체제마다 디렉토리 인자가 다름.. \ /
        if os.path.isdir(fullpath):   # isdir(f) 쓰면 이름만 주니까
            print(f"{fullpath}")
            dumpdir(fullpath)   # 재귀호출
        else:
            print("\t" + f)


def main():
    dumpdir('\\temp')


main()