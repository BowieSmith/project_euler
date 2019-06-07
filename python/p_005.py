# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import p_003
import collections

# get prime factors for all values in range(start, stop + 1)
# of prime factors, find max factor count for each
#   e.g. 6=2*3, 9=3*3, so max factor count for 3 is 2
# multiply all primes factors together
def smallest_divisible(start, stop):
    prime_counts = {}
    for i in range(start, stop + 1):
        if p_003.is_prime(i):
            factors = [i]
        else:
            factors = p_003.prime_factors(i)
        this_prime_counts = collections.Counter(factors)
        for key,val in this_prime_counts.items():
            if key not in prime_counts:
                prime_counts[key] = val
            else:
                if val > prime_counts[key]:
                    prime_counts[key] = val

    smallest = 1
    for key,val in prime_counts.items():
        smallest *= key ** val

    return smallest

if __name__ == "__main__":
    ans = smallest_divisible(1,20)
    print(ans)
