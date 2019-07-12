# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

def nth_permutation(lst, n):
    perm = []
    lst = list(lst)
    lst.sort()
    for i in range(len(lst) - 1):
        total_left = len(lst)
        perm.append(lst.pop(n // math.factorial(total_left - 1)))
        n %= math.factorial(total_left - 1)
    perm.extend(lst)
    return perm

if __name__ == "__main__":
    # use 999_999 since 0 indexing is used
    ans = ''.join(nth_permutation('0123456789', 999_999))
    print(ans)
