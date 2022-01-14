n = int(input())

answers = 0
for i in range(n):
    a = list(map(int, input().split()))
    zeros = a.count(0)
    # print(zeros)
    if(zeros == 0 or zeros ==1):
        answers+=1

print(answers)

