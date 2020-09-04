import copy

def main():
    list0 = ['a', 'b']
    list1 = [list0, 1, 2]
    list2 = copy.deepcopy(list1)
    list2[0][1] = 'c'
    list2[1] = -1
    print(list1)
    print(list2)
    print(list0)



main()