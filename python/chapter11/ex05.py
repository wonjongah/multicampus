def main():
    score = [45, 89, 72, 53, 94]
    for s in map(lambda x: x / 2, score):
        print(s, end=", ")


main()