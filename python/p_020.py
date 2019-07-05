# Find the sum of the digits in the number 100!

def fact(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

def sum_of_digits(n):
    digits = map(int, str(n))
    acc = 0
    for digit in digits:
        acc += digit
    return acc

if __name__ == "__main__":
    ans = sum_of_digits(fact(100))
    print(ans)
