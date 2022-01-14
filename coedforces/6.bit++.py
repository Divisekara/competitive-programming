n = int(input())
result = 0

for i in range(n):
    if("++" in input()):
        result+=1
    else:
        result-=1
    
print(result)

