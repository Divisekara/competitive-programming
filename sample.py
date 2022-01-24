import time
from tracemalloc import start

from pyparsing import restOfLine

start_time = time.time()

result = 0
for i in range(0,100000):
    result += i

print(result)

time.sleep(1)
end_time = time.time()

print("time consumed = {0:.5f}ms ".format((end_time-start_time)*1000))