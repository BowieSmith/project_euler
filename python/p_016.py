# What is the sum of the digits of the number 2^1000?

def sum_digits(n, p):
    return sum(map(int, list(str(n ** p))))

if __name__ == "__main__":
    ans = sum_digits(2, 1000)
    print(ans)
