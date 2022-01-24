import time
start_time = time.time()

memo = {}


def fib_memo(n, memo):
    if(n in memo.keys()):
        return memo[n]

    elif(n<=2):
        f = 1
        memo[n] = 1

    else:
        if(n in memo.keys()):
            f = memo[n]
        else:
            f = fib_memo(n-1, memo) + fib_memo(n-2, memo)
            memo[n] = f
    
    return f
    

term = fib_memo(999, memo)
end_time = time.time()

print(term)

print("{:.10f}ms".format((end_time-start_time)*1000))


