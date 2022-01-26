T = int(input())

for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    S = input()
    ans = 0 
    score =0
    for i in range(0,int(N/2)):
        if(S[i] != S[N-1-i]):
            score+=1

    if(score==K):
        ans = 0
        
    else:
        ans = abs(score-K)


    print("Case #{}: {}".format(t, ans))
