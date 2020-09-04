import time

start = time.time()  # 함수가 수행되는 시간 측정
for a in range(1000):
    print(a)
end = time.time()
print(end - start)

# 출력하는 함수와 메모리 내에서 합을 구하는 시간은 다름...
# sw 성능 높이는 방법, 입출력 최소화하기, 데이터를 모았다가 한 번에 입출력하기

start = time.time()
sum = 0
for i in range(1000):
    sum += i
end = time.time()

print(end - start)