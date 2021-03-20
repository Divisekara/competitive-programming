n  = int(input().strip())

d = {}
scores = []

for i in range(n):
    name = input().strip()
    score = float(input().strip())
    scores.append(score)
    if(score not in d.keys()):
        d[score] = [name]
    else:
        d[score] += [name] 

scores = sorted(list(set(scores)))

# print(d)

answer = d[scores[1]]

answer.sort()

for i in answer:
    print(i)