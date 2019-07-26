def fib_dp(n: int, memo: list):
    result = 0
    if memo[n] != None:
        return memo[n]
    if n == 1 or n==2:
        result = 1
    else:
        result = fib_dp(n-1, memo) + fib_dp(n-2, memo)
    memo[n] = result
    print(memo)
    return result

def fib_bottom_up(n):
    if n ==1 or n ==2:
        return 1
    else:
        bottom = [None] *(n+1)
        bottom[1] = bottom[2] =  1        
        for i in range(3, n+1):
            bottom[i] = bottom[i-1] + bottom[i-2]
        print(bottom)
        return bottom[n]

n = 15
print(fib_dp(n, [None]*(n+1)))
print(fib_bottom_up(n))

