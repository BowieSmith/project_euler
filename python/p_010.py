# Find the sum of all the primes below two million.

import p_003

def primes_below(n):
    prime_gen = p_003.primes()
    cur = next(prime_gen)
    while cur < n:
        yield cur
        cur = next(prime_gen)

if __name__ == "__main__":
    ans = sum(primes_below(2_000_000))
    print(ans)
