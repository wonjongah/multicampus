import sys
from myapp import Application, MenuItem

class NotepadApp(Application):  # 메모장의 어플리케이션을 생각해라, 메뉴를 운영(소유) / 범용적이지 않음, 내가 만들고 싶은 어플에 따라 모양 바뀜
    def __init__(self):
        super().__init__()  # Menu(), create_menu
        # 열기 저장하기 목록보기 종료하기
        # self.menu.add(MenuItem("열기", self.open))  # 자기자신의 오픈메서드.. 그냥 open 쓰면 함수 오픈
        # ...

    def create_menu(self, menu):
        menu.add(MenuItem("열기", self.open))
        menu.add(MenuItem("저장", self.save))
        menu.add(MenuItem("목록보기", self.print_list))
        menu.add(MenuItem("종료", self.exit))

    def open(self):
        print("열기를 실행합니다")

    def save(self):
        print("저장을 실행합니다")

    def print_list(self):
        print("목록보기를 실행합니다")

    def exit(self):
        sys.exit(0)  # 0으로 exit는 정상적인 종료



def main():
    app1 = NotepadApp()
    app1.run()

if __name__ == "__main__":    # 이것도 모듈로 쓸 수 있다, 단독으로 실행될 때만 main() 실행해라
    main()                    # 다른 곳에서 모듈로 쓰이면 main()이 실행이 되지 않는다는 뜻!!
                              # run의 무한루프에도 안 빠짐