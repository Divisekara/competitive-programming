n,k =list(map(int, input().split()))
scores = list(map(int, input().split()))

key = scores[k-1]

next = 0
for i in scores:
    if(i>=key and i>0):
        next += 1

print(next)
