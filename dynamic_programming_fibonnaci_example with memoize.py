import time
start_time = time.time()

memo = {}
# memoize using
# dynamic programming
# bigO(n)


def fib_memo(n, memo):
    if(n in memo.keys()):
        f = memo[n]

    elif(n<=2):
        f = 1
        memo[n] = 1

    else:
        f = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        memo[n] = f
    
    return f
    

term = fib_memo(1000, memo)
end_time = time.time()

print(term)

print("{:.10f}ms".format((end_time-start_time)*1000))


