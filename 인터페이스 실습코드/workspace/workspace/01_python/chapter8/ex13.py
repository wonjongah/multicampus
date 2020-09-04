def main():
    name = "한결"
    age = 16
    height = 162.5
    print("이름:{}, 나이: {}, 키: {}".format(name, age, height))
    print("이름:{:s}, 나이: {:d}, 키: {:f}".format(name, age, height))
    print("이름:{:4s}, 나이: {:3d}, 키: {:.2f}".format(name, age, height))

    print()

    age = 16
    height = 162.5
    print("이름:{0}, 나이: {1}, 키: {2}".format(name, age, height))
    print("이름:{2}, 나이: {1}, 키: {0}".format(height, age, name))
    print("이름:{name}, 나이: {age}, 키: {height}".format(age=20, height=160.9,
    name="길동"))

    print()

    boy = {"name": "길동", "age":20, "height":160.9}    # 딕셔너리
    print("이름:{0[name]}, 나이:{0[age]}, 키:{0[height]}".format(boy))

    # 우린 이걸 쓸 거임 3.8인가부터 적용
    print()

    print(f"이름: {name}, 나이: {age}, 키: {height:.2f}")
main()