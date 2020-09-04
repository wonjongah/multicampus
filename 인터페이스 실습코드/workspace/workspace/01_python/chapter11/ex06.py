song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()
for c in song:   # c에는 글자 단위로 하나씩 들어감
    if c.isalpha() == False:
        continue

    c = c.lower()   # 혹시 해서 소문자로
    if c not in alphabet:   # 키로 있냐 없냐
        alphabet[c] = 1  # 처음 등장함, 사전에 넣어야 함, 값 1 대입, add
    else:
        alphabet[c] += 1 # 기존에 있던 값, 값 추가, update


def get_value(x):   # x는 튜플로 가정
    return x[1]
 
 # chapter10 의 ex01을 카운트 개수로 정렬하고 싶다

alphabet_list = list(alphabet.items())  # 정렬하려면 list의 sort필요
# alphabet_list.sort(key=get_value, reverse=True)  # 키워드인수
alphabet_list.sort(key=lambda x: x[1], reverse=True) # reverse=True --> 내림차순
for a, c in alphabet_list:
    print(f"{a} : {c}")