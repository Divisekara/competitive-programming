T = int(input())

def sorting(L):
    M = [' ', 'A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ans = 0
    for k in range(0, len(L)-1):
        word1 = L[k]
        word2 = L[k+1]
        for j in range(0, len(word1)):
            try:
                w1 = word1[j]
            except:
                break
            try:
                w2 = word2[j]
            except:
                L[k], L[k+1] = L[k+1], L[k]
                ans +=1
                break

            if(M.index(w1) > M.index(w2)):
                L[k], L[k+1] = L[k+1], L[k]
                ans+=1
                break
            elif(M.index(w1) == M.index(w2)):
                continue
            else:
                break


    return ans, L

for t in range(1,T+1):
    N = int(input())
    L=[]
    for j in range(N):
        L.append(input().strip())
    
    ans = sorting(L)

    print("Case #{}: {}".format(t, ans))

# 1
# 3
# Elvis Stojko
# Evgeni Plushenko
# Kristi Yamaguchi
