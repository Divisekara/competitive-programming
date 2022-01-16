n = int(input())

word = list(input())

answer = 0
previous = word[0]
for i in range(1,len(word)):
    if(previous == word[i]):
        answer+=1
    else:
        previous = word[i]

print(answer)

#  RRRGGGRRR

