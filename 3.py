T = int(input())

for t in range(1, T + 1):
    B = list(map(int, input().strip().split()))[1]
    ar = sorted(list(map(int, input().strip().split())))
    

    print("Case #{}: {}".format(t, ans))
