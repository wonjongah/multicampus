def calcsum(n):
    total = 0
    for num in range(n + 1):
        total += num

 #   return total
 # 돌아갈 때 데이터를 가지고 가냐 안 가지고 가냐
 # 돌아갈 땐 return, 그리고 값을 가지고 가야 함
 # 돌아갈 때 return 안 하고 돌아가면 None
 # def은 호출할 때보다 먼저 선언해야 한다


print(" ~ 4 =", calcsum(4))
print(" ~ 10 =", calcsum(10))
