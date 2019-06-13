# What is the largest prime factor of the number 600851475143 ?

import math

def is_prime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    for i in range(3, math.ceil(n ** (1/2)) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes():
    current = 1
    while True:
        current += 1
        if is_prime(current):
            yield current

# finds first prime factor. Returns -1 if no such factor exists
def first_factor(n):
    if n == 2:
        return -1
    for p in primes():
        if n % p == 0:
            return p
        if p >= n ** (1/2):
            return -1

# return list of prime factors
def prime_factors(n):
    factors = []
    current = n
    while True:
        factor = first_factor(current)
        if factor == -1:
            if current != n:
                factors.append(current)
            return factors
        else:
            factors.append(factor)
            current = current // factor

if __name__ == "__main__":
    ans = prime_factors(600851475143)[-1]
    print(ans)
