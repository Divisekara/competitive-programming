n = int(input())
L = list(map(int, input().split()))
total = sum(L)
half = total/2
L.sort()
L.reverse()
no_coins = 0
sum_ = 0

for i in L:
    sum_+=i
    no_coins+=1
    # print(half, sum_)
    if(sum_>half):
        break

print(no_coins)



