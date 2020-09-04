import random

pae = [n for n in range(1, 49)]
print("고스톱 패 섞기 및 패 분배")
print("패의 수 : ", len(pae))

i = int(input("게임 인원 수: "))

random.shuffle(pae)

print("사용자 패")

for a in range(1, i+1):
    print(a, "번째 사용자 ", end="")
    pae1 = random.sample(pae, 7)
    print(pae1)
    nam_pae = set(pae) - set(pae1)
print("남은 패(", len(pae) - (i * 7), ")장")
print(list(nam_pae))


# 내가 한 것