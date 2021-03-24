import math

T = int(input())

for i in range(1, T+1):
    v,d = list(map(int, input().split()))
  
    ans = math.degrees(math.asin(d*9.8/(v*v))) / 2

    print("Case #{}: {:6f}".format(i, ans))
