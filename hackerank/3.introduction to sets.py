n = int(input().strip())

x = list(set(list(map(int, input().strip().split()))))
print(sum(x)/ len(x))