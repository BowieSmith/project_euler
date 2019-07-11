# Evaluate the sum of all the amicable numbers under 10000.

import p_012

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
def d(n):
    divisors = p_012.factors(n)
    divisors.remove(n)
    return sum(divisors)

if __name__ == "__main__":
    sum_of_amicables = 0

    for i in range(2, 10_000):
        div_sum = d(i)
        if d(div_sum) == i and div_sum != i:    # do not include perfect numbers
            sum_of_amicables += i

    print(sum_of_amicables)
