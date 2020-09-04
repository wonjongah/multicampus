print(ord('a'))  # ord 유니코드로!!takes string argument of a single Unicode character and return its integer Unicode code point value


print(chr(98))  # 유니코드를 알파벳으로
for c in range(ord('A'),ord('Z')+1):
    print(chr(c), end='')