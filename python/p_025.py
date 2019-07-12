# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# Start with: 1 1 2 3 ...

def fib_gen(first, second):
    a, b = first, second
    while True:
        yield a
        a, b = b, a + b

# generates fib sequence tuples as: (index, fib_val, no_digits)
def indexed_fib_gen(first, second):
    gen = fib_gen(first, second)
    index = 1
    while True:
        current = next(gen)
        yield (index, current, len(str(current)))
        index += 1

if __name__ == "__main__":
    gen = indexed_fib_gen(1, 1)
    cur = next(gen)
    while cur[2] < 1000:
        cur = next(gen)
    ans = cur[0]
    print(ans)
