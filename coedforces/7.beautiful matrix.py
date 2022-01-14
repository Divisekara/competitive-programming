for i in range(1,6):
    row = list(map(int, input().split()))
    if(1 in row):
        print(abs(i-3) + abs(row.index(1)+1-3))
        break