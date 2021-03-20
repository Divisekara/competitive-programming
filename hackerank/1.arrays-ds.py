n = int(input().strip())

array = list(map(int, input().strip().split()))

for i in range(n//2):
    x = array.pop(i)
    y = array.pop(-1-i)
    array.insert(i, y)
    array.insert(n-1-i, x)

print(" ".join(list(map(str, array))))


