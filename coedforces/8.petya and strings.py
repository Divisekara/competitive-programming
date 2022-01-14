from tkinter import N


word1 = input().casefold()
word2 = input().casefold()

n = len(word1)

for i in range(n):
    if(word1[i] > word2[i]):
        print(1)
        break
    elif(word1[i] < word2[i]):
        print(-1)
        break

else:
    print(0)