from multiprocessing.sharedctypes import Value


word = input()

while(len(word)>0):
    if(word[:3]=="WUB"):
        word = word [3:]
    else:
        try:
            idx = word.index("WUB")
        except ValueError:
            idx = len(word)
        print("".join(word[:idx]), end=' ')
        word = word[idx:]

# answer 1
# print(*input().split('WUB'))

# answer 2
# def Dubstep():
#     s = input()
#     a = s.replace("WUB", " ", s.count("WUB"))
#     print(a)
 

# L = [1,2,3,4,5]
# s ='Iam'
# print(*s)
# # this is prefix operator of asterisk
# # this is used before a variable
# # there are many use cases of asterisk in python
# # here we use the unpacking property for a string/tuple/list
# # so any iterable data type can be unpacked using the * 
# # in printing the default seperator is ' ' a single space,
# # if we want we can change it to be defined

# print(*'asitha', sep=' redda ')



