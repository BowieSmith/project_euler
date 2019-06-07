# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(start, stop):
    return sum(x*x for x in range(start, stop + 1))

def square_of_sum(start, stop):
    return sum(x for x in range(start, stop + 1)) ** 2

if __name__ == "__main__":
    ans = abs(sum_of_squares(1, 100) - square_of_sum(1, 100))
    print(ans)
