def main():
    dic = {
        'boy': '소년',
        'school': '학교',
        'book': '책'
    }
    print(dic)


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


print(alphabet)   # 추가된 순서로.., 가독성 안 좋음

key = list(alphabet.keys())  # sort 사용하기 위해 리스트로 변환
key.sort()
for c in key:
    num = alphabet[c]
    print(c, '=>', num)

# 밸류 자체는 정렬 가능, alphabet.values()하면 된다, 근데 밸류로 키를 얻지 못함
# 이럴 때는 .item() 쓴다, 키와 밸류 튜플로 변환


main()