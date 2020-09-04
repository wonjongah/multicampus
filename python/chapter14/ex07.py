def main():
    f = open("live.txt", "rt")

    f.seek(12, 0)  # 한글 중간에 걸침
    text = f.read()
    f.close()
    print(text)

main()