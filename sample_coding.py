import string


a = 10 # integers storage 8 bytes
b = 10.00 # floats storage 
c = True # bool can have only two values True, False, memory storage is 1 bit

d = {'a':10, 'b':20, 'c':'Sample'} # we store key value pairs inside a dictionary 
# d = {key:value}


# print(10/3) # original division
# print(11//3) # floor division
# print(10%3) # modulo division
    #0123456
    #-6-5-4-3-2-1
e = "Asitha"

# string and list both data types have len keyword to output the size of the array
# print(len(e))
# print(e[2:5])
# print(e[-1:3:-1]) 
# # slicing of a string and list
# print(e[::-1])

idx = e.index('t')
# print('idx = ' , str(idx)) # theres an error

# "ASithHA".capitalize()

L = [1,2,3,"a", "asitha", True, [1,2,3,4] ] #Inside a list any data type can be stored
B = L # both these names point to one memory location 
C = L.copy()
D = L[:]
L.append("Asitha divisejara")
B.append("Thushani chadrasekara")
print(id(L))
print(id(B))
print(B,'\n', L) # \n - newline character

# print(type(c))




