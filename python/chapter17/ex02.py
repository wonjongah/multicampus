class Seq:
    def __init__(self, data):
        self.data = data
        self.index = -2  # 플러스 2하니까 먼저 -2로 초기화

    def __iter__(self):
        self.index = -2  # for문 시작할 대 __iter__부터 되므로!
        return self

    def __next__(self):
        self.index += 2 # 인덱스 먼저 2 증가!
        if self.index >= len(self.data):
            self.index = -2
            raise StopIteration

        return self.data[self.index:self.index+2]  # 슬라이싱으로 뽑아서 리턴


def main():

    solarterm = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")  # Seq 클래스, 객체 만들어서 리턴
    for k in solarterm:
        print(k, end=",")

    print()

    for k in solarterm:   # 인덱스 맨 끝으로.. 읽을 수 없음, 즉 넥스트 안의 레이즈 앞에 다시 인덱스를 지정해줌
        print(k, end=',')


main()