import time

from pyparsing import restOfLine

start_time = time.time()

result = 0
for i in range(-1000000,1000000):
    if(i%2==0):
        pass
    result += i

print(result)


end_time = time.time()
print("time consumed = {0:.5f}ms ".format((end_time-start_time)*1000))



# print("{0:.5f}".format(123456789.123456789))
