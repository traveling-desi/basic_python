t1, t2, n = map(int, raw_input().split())


def memo(f):
    cache= {}
    
    def _f(n):
        try:
            ans = cache[n]
        except:
            ans = f(n)
            cache[n] = ans
        return ans
            
    return _f

@memo     
def fib(n):
    if n == 3:
        return t1 + t2**n
    elif n == 2:
        return t2
    elif n == 1:
        return t1
    return fib(n-2) + fib(n-1)**2


print fib(n)
