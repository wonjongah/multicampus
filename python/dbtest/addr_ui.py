# 출력, 즉 화면에 보이는 것들 모음
from addr_models import Addr

def print_list(total, rows):
    print("===============================")
    print("No  이름     전화번호     주소    ")
    for ix, row in enumerate(rows, 1):
        print(f"{ix} : {row.name:10} {row.phone:10} {row.addr}")  # 로우 뒤의 :숫자 -> 길이! 열 글자 폭에 맞춰서 출력

    print("===============================")
    print(f"(총 {total} 건)")


def input_addr_info(name):

    addr = input("입력할 주소를 입력하세요 : ")

    phone = input("입력할 전화번호를 입력하세요 : ")
    return Addr(name, phone, addr)   # 튜플되어 리턴

def input_new_addr(data):
    phone = input(f"전화번호({data.phone}) : ")
    if not phone:
        phone = data.phone
    addr = input(f"주소({data.addr}")
    if not addr:
        addr = data.addr

    return Addr(data.name, phone, addr)