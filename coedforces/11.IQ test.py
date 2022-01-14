n = int(input())
numbers = list(map(int, input().split()))


evens = 0
last_even_idx = 0
odds = 0
last_odd_idx = 0

for i in range(n):
    number = numbers[i]
    if(number%2==0):
        evens+=1
        last_even_idx = i
    else:
        odds+=1
        last_odd_idx = i

    if(evens>=1 and odds>=1 and evens!=odds):
        if(odds==1):
            print(last_odd_idx+1)
        elif(evens==1):
            print(last_even_idx+1)
        break



    
