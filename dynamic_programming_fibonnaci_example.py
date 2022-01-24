from threading import Timer

import time
start_time = time.time()

def fib(n,):
    if(n<2):
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    return f

term = fib(35)
print(term)

end_time = time.time()

print("{:.5f}ms".format((end_time-start_time)*1000))





