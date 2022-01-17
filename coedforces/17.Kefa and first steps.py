from multiprocessing.connection import answer_challenge


n = int(input())
L = list(map(int, input().split()))

answer = 0
previous = L[0]
temp = 0

for i in range(1, len(L)):
    temp+=1
    if(previous>L[i]):
        if(answer<temp):
            answer = temp
        temp = 0
    # print(L[i], answer, temp)
    previous = L[i]

if(answer == 0 or answer<temp+1):
    answer = temp +1
    

print(answer)



