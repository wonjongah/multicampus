import random
for i in range(5):
    print(random.randrange(1,10))

print()

for i in range(5):
    print(random.uniform(1, 10))

print()

for i in range(5):
    print(random.randint(1, 10))  # end 포함

print()

food = ["자장면", "짬뽕", "탕수육", "군만두"]
print(random.choice(food))

print()

print(food)
random.shuffle(food)   # 순서 섞임 call by reference
print(food)
print()
print(random.sample(food,2))

print()

nums = random.sample(range(1,46), 6) # 로또
nums.sort()
print(nums)