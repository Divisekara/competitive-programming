T = int(input())

def solve():
    score = 0

    for i in range(0, N//2):
        if(S[i] != S[N-i-1]):
            score+=1
    
    return abs(K-score)




for t in range(1,T+):
    N, K = list(map(int, input().split() ))
    S = input()
    ans = solve()

    print("Case #{}: ans".format(t,ans))
