n = int(input().strip())

d = {}

for i in range(n):
    temp = input().strip().split()
    name, scores = temp[0], temp[1:]
    d[name] = list(map(float, scores))

parti = input().strip()

x = round(sum( d[parti]) / (len(d[parti])), 2) 

print('{:.2f}'.format(x))
