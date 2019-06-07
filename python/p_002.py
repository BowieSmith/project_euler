# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibs():
    a,b = 0,1
    while True:
        a,b = b,a+b
        yield a

def fibs_under(n):
    g = fibs()
    current = next(g)
    while current < n:
        yield current
        current = next(g)

ans = sum(x for x in fibs_under(4_000_000) if x % 2 == 0)

print(ans)
