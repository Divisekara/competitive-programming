from re import L


pos = input()

if('0000000' in pos or '1111111' in pos):
    print("YES")
else:
    print("NO")