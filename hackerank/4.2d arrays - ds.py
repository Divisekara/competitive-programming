L = []
for i in range(6):
    line = list(map(int, input().strip().split()))
    L.append(line)


dp  = [[0 for a in range(4) ] for b in range(4) ]

answer = 0
for i in range(1,5):
    for j in range(1,5):
        answer = L[i-1][j-1] + L[i-1][j] + L[i-1][j+1] + L[i][j] + L[i+1][j-1] + L[i+1][j] + L[i+1][j+1]

        # print(answer)

        dp[i-1][j-1] = answer

for k in dp:
    answer = max(answer,max(k))

print(answer)


# 0 -4 -6 0 -7 -6
# -1 -2 -6 -8 -3 -1
# -8 -4 -2 -8 -8 -6
# -3 -1 -2 -5 -7 -4
# -3 -5 -3 -6 -6 -6
# -3 -6 0 -8 -6 -7
