def XOR (a, b):
    if a != b:
        return 1
    else:
        return 0
    
def XOR_check(L):
    result= XOR(L[0], L[1])
    for i in range(2,len(L)):
        result = XOR(result, L[i])
    
    return result


T = int(input())

for t in range(1, T + 1):
    N  = int(input)
    
    A = []
    B = []
    R = []
    C = []
    for i in range(0,N):
        row = list(map(int, input().split()))
        A.append(row)
    
    for i in range(0, N):
        row = list(map(int, input().split()))
        B.append(row)

    R = list(map(int, input().split()))
    C = list(map(int, input().split()))

    for k in range(0, N):
        for m in range(0, N):
            if (A[k][m] == -1):
                cost = B[k][m]
                Ri = R[k]
                Cj = C[m]

    print("Case #{}: {}".format(t, ans))
