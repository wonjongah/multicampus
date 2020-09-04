import util   # 어느 디렉토리에서 찾나?
              # 같은 디렉토리에서 찾지 않는다, 워킹디렉토리에서 찾는다
              # chapter15에서 찾는다
              # sys.path 순서로 찾는다
import sys

print(util.INCH)

for path in sys.path:
    print(path)