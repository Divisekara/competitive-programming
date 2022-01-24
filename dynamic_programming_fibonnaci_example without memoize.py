from threading import Timer

import time
start_time = time.time()

def fib(n):
    if(n<=2):
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    return f

term = fib(2)
end_time = time.time()

print(term)
print("{:.10f}ms".format((end_time-start_time)*1000))



# we can see that without using the memoize the algorithm time complexity exponentially grwos which is two to the power of n = 2^n
# the time gets double almost everytime we increase the number by 1.
# for the 40th term it takes more than 20seconds to calculate the fibbonacci








