# tutorial - https://www.geeksforgeeks.org/submatrix-sum-queries/

# Function preoprocess input mat[M][N]
# This funcction mainly fills aux[M][N]
# such that aux[i][j] stores sum 
# sum of elements from (0,0) to (i,j)

def preProcess(mat, aux): # making the auxillary matrix

    # print(mat)

    # copy first row of mat[][] to aux[][]
    for i in range(0, N, 1):
        aux[0][i] = mat[0][i]
    
    # print(aux)
    
    # do column wise sum
    for i in range(1, M, 1):
        for j in range(0, N, 1):
            aux[i][j] = mat[i][j] + aux[i - 1][j]
    
    # print(aux)

    # do row wise sum
    for i in range(0,M, 1):
        for j in range(1, N, 1):
            aux[i][j] += aux[i][j-1]


    # print(aux)


# A O(1) time function to compute sum of submatrix
# between (tli, tlj) and (rbi, rbj) using aux[][]

def sumQuerry(aux, tli, tlj, rbi, rbj):
    # results is now sum of elments between (0,0) and (rbi, rbj)
    res = aux[rbi][rbj]

    # now we have to remove the sum of elements between (0,0) and (tli -1 , tlj) 

    if(tli > 0):
        res = res - aux[tli - 1][rbj]

    # now we have to remove the sum of elements between (0,0) and (tli , tlj - 1) 
    if(tlj > 0):
        res = res - aux[rbi][tlj - 1]
    
    # Add aux[tli-1][tlj-1] as elements between (0, 0) and (tli-1, tlj-1) are subtracted twice
    if(tli > 0 and tlj > 0):
        res = res + aux[tli-1][tlj-1]


mat = [[1, 2, 3, 4, 6],
        [5, 3, 8, 1, 2],
        [4, 6, 7, 5, 5],
        [2, 4, 8, 9, 4]]

M = 4
N = 5

aux = [[0 for i in range(N)] for j in range(M)]

preProcess(mat, aux)

