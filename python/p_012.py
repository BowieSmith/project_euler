# What is the value of the first triangle number to have over five hundred divisors?

import p_003
import itertools

# closed form solution for nth triangular number
def triangular(n):
    return (n * (n + 1)) // 2

# infinite generator for triangular numbers
def triangular_gen():
    cur = 1
    while True:
        yield triangular(cur)
        cur += 1

# get product of elements of iterable 
def product(it):
    cur = 1
    for i in it:
        cur *= i
    return cur

# get factors using all combinations of prime factorization
def factors(n):
    prime_factors = p_003.prime_factors(n)
    factors = set()
    factors.add(1)
    for i in range(1, len(prime_factors) + 1):
        for prime_subset in itertools.combinations(prime_factors, i):
            factors.add(product(prime_subset))
    return factors

if __name__ == "__main__":
    tri = triangular_gen()
    cur = next(tri)
    while len(factors(cur)) < 500:
        cur = next(tri)
    ans = cur
    print(ans)
