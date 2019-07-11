# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import p_021

if __name__ == "__main__":
    abundant_nums = set()
    for i in range(1,30_000):
        if p_021.d(i) > i:                  # if sum of divisors > i
            abundant_nums.add(i)

    nums_sum_of_abundant_pairs = set()

    for i in range(1, 30_000):
        for j in range(1, i):
            if j in abundant_nums:
                if i - j in abundant_nums:
                    nums_sum_of_abundant_pairs.add(i)
                    break

    positive_ints = set(range(1, 28124))    # positive ints under 28124
    nums_not_sum_of_abundant_pairs = positive_ints - nums_sum_of_abundant_pairs

    print(sum(nums_not_sum_of_abundant_pairs))
