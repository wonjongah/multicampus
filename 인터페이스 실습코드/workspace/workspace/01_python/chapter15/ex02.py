class Stack:
    def __init__(self, size=5):
        self.data = []
        self.size = size

    def push(self, push_value):
        if len(self.data) == self.size:  # full
            print("스택이 가득 찼습니다. pop()을 통해 지워주세요")
            return
        else:
            self.data.append(push_value)
            print(push_value, "값 푸쉬")

    def pop(self):
        if len(self.data) == 0:     # empty
            print("스택이 비어있습니다. push()를 통해 값을 채워넣을세요")
            return
        else:
            self.data.pop()
            print("pop!")

    def clear(self):
        self.data = []
        print("클리어")

    def print_car(self):
        print(self.data)

    def __str__(self):
        return f"<Stack size:({self.size}), data:({self.data})>"

def main():

    s1 = Stack()
    s1.push(5)
    s1.push(2)
    print(s1)
    s1.pop()
    print(s1)
    s1.clear()
    s1.pop()


main()