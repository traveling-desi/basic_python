'''
We define a modified Fibonacci sequence using the following definition:

Given terms  and  where , term  is computed using the following relation:
For example, if term  and , term , term , term , and so on.

Given three integers, , , and , compute and print term  of a modified Fibonacci sequence.

Note: The value of  may far exceed the range of a -bit integer. Many submission languages have libraries that can handle such large results but, for those that don't (e.g., C++), you will need to be more creative in your solution to compensate for the limitations of your chosen submission language.

Input Format

A single line of three space-separated integers describing the respective values of , , and .

Constraints

 may far exceed the range of a -bit integer.
Output Format

Print a single integer denoting the value of term  in the modified Fibonacci sequence where the first two terms are  and .

Sample Input

0 1 5
Sample Output

5
Explanation

The first two terms of the sequence are  and , which gives us a modified Fibonacci sequence of . Because , we print term , which is .
'''


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
