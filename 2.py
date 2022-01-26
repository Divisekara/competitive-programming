T = int(input())

def check(L):
    C = len(L[1])
    R = len(L)

    L_check_ver = False
    L_check_hor = False

    for i in range(0,R):

        for j in range(0, C):
            if(L[i][j] != 1):
                continue
            else:
                if(L[i][j+1] !=1 ):
                    pass
                
                if(L[i+1][j] !=1):
                    pass

                


for t in range(1, T + 1):
    R, C = list(map(int, input().split()))

    L=[]
    for j in range(R):
        row = list(map(int, input().split()))
        L.append(row)
    

    print("Case #{}: {}".format(t, ans))
