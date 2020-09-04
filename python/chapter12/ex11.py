import random
def init(user_num): # 패 섞기
    deck = list(range(1, 49))   # range(0, 48)이 컴퓨터에선 더 편리
    random.shuffle(deck)

    users = [[] for _ in range(user_num)]  # 사용자 수만큼 이중리스트 []수 가변적, 사람 수
    return deck, users


def assign(deck, users):
    for _ in range(7):  # 지금은 한 장씩 사람들에게 돌리는 것, 루프 바꾸면 한 사람에게 일곱장 할당하고 그다음 또 할당
        for user_card in users:  # 사용자 수만큼 돌겠다
            card = deck.pop()  # 다 원본가지고 작업, 콜바이레퍼런스
            user_card.append(card)

def print_result(deck, users):
    print("사용자 패")
    for ix, user_cards in enumerate(users, 1):
        print(f"{ix} 번째 사용자 : ", user_cards)
    print(f"남은 패({len(deck)}장)")
    print(deck)

def main():
    user_num = int(input("게임 인원수 : "))
    deck, users = init(user_num)
    assign(deck, users)
    print_result(deck, users)


main()