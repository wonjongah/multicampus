import pickle
import os

def save(name, data):
    try:
        with open(name, "wb") as f:   # f = open(name, "wt")과 동일
            pickle.dump(data, f)
    except Exception as e:
        print(e)
    # f.close()

def load(name):
    try:
        with open(name, "rb") as f:   # f = open(name, "wt")과 동일
            data = pickle.load(f)
            return data

    except Exception as e:
        print(e)
    # f.close()


def main():
    data = [
        [1, 2, 3, 54, 45],
        [7, 8, 3, 4, 5],
        [1, 12, 13, 4, 25]
        ]


    save("./data/data2.dat", data)   # 파일은 없으면 만들어지지만 디렉토리는 만들어지지 않음

    data2 = load("./data/data2.dat")
    print(data2)



main()