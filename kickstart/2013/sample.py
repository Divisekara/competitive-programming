def sorting(L):
    M = [' ', 'A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ans = 0
    for i in range(0,len(L)):
        for k in range(0, len(L)-1):
            word1 = L[k]
            word2 = L[k]
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

    
    return ans

# print(sorting(L))

if('asitha' > 'Asitha'):
    print(True)
else:
    print(False)


L = ['asitha', 'Asitha']

L.sort()

print(L)



