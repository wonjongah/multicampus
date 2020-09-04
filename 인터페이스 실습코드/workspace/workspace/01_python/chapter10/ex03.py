def main():
    twox = {2, 4, 6, 8, 10, 12}
    threex = {3, 6, 9, 12, 15}

    print("교집합", twox & threex)
    print("합집합", twox | threex)
    print("차집합", twox - threex)
    print("차집합", threex - twox)
    print("배타적 차집합", twox ^ threex)



main()