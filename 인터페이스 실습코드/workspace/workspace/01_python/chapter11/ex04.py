def main():

    score = [45, 89, 72, 53, 94]
    for s in filter(lambda x: x < 60, score):
        print(s)


main()