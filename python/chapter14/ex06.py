def save(name, data):
    try:
        with open(name, "wt") as f:   # f = open(name, "wt")과 동일
            for i in data:
                i = map(str, i)   # 문자열로 바꿔서 리스트로 i = str(l)
                row = ','.join(i)  # ,로 엮는다, 대신 join은 문자열만
                f.write(row + "\n")  # 문자열에서 엘리먼트는 문자,,  h e l 5 3 2 ,이런식
    except Exception as e:
        print(e)
    # f.close()

def load(name):
    try:
        with open(name, "rt") as f:   # f = open(name, "wt")과 동일
            rows = f.readlines()
            data = []
            for row in rows:
                print(row, end='')  # 한 줄이 개별 문자열, 이미 끝에 개행문자 있어서 end = ''
                new_row = row.split(',')
                print(new_row)
                new_row = list(map(int, new_row))
                print(new_row)
                data.append(new_row)
            return data   # with 코드블럭 벗어난 작업, 자동으로 크로즈

    except Exception as e:
        print(e)
    # f.close()


def main():
  #  data = [
   #     [1, 2, 3, 54, 45],
    #    [7, 8, 3, 4, 5],
     #   [1, 12, 13, 4, 25]
      #  ]

   # save("data.csv", data)
    data = load("data.csv")
    print(data)



main()