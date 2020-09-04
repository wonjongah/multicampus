def flunk(s):
    return s < 60

def is_even(s):
    return s % 2 == 0

def fliter(fn, lst):   # fn = flunk
    new_list = []      # 비어있는 리스트 만듦
    for a in lst:
        if fn(a):
            new_list.append(a)
    return new_list

def main():
    score = [45, 89, 72, 53, 94]
    for s in filter(is_even, score):
        print(s)

    even_list = list(filter(is_even, score))
    print(even_list)

main()
