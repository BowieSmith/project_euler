# What is the 10 001st prime number?

import p_003

def nth_prime(n):
    prime_gen = p_003.primes()
    for i in range(n - 1):
        next(prime_gen)
    return next(prime_gen)

if __name__ == "__main__":
    ans = nth_prime(10_001)
    print(ans)
