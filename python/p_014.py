# Which starting collatz number under one million produces the longest sequence?

def collatz_gen(n):
    while True:
        if n == 1:
            return
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        yield n

def collatz_seq_size(n):
    size = 1
    for _ in collatz_gen(n):
        size += 1
    return size

if __name__ == "__main__":
    col_num = 1
    max_seq_len = 0
    for i in range(1, 1_000_000):
        size = collatz_seq_size(i)
        if size > max_seq_len:
            max_seq_len = size
            col_num = i
    print(col_num)
