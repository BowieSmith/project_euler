# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# enumerate all a,b,c where a < b < c and a + b + c == 1000
def enumerate_choices(n):
    for a in range(1, n // 3):
        for b in range(a + 1, n - a + 1):
            if b < n - a - b:
                yield (a, b, n - a - b)
            else:
                break

def find_first_pyth_trip(n):
    choice_gen = enumerate_choices(n)
    for a,b,c in choice_gen:
        if a**2 + b**2 == c**2:
            return (a,b,c)

if __name__ == "__main__":
    trip = find_first_pyth_trip(1000)
    ans = trip[0] * trip[1] * trip[2]
    print(ans)
