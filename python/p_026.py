# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def decimal_expansion_unit_fraction(d):
    expansion = []
    dividend = 10
    current_index = 0
    while True:
        expansion.append((dividend // d, dividend))
        dividend = (dividend % d) * 10
        if expansion[-1] == (0,0):
            break
        if expansion.index(expansion[-1]) != len(expansion) - 1:
            break
    return expansion

def pretty_format(d):
    expansion = decimal_expansion_unit_fraction(d)
    s = '0.'
    if expansion[-1] == (0,0):
        expansion.pop()
        s += ''.join(map(lambda e: str(e[0]), expansion))
    else:
        index = expansion.index(expansion[-1])
        expansion.pop()
        s += ''.join(map(lambda e: str(e[0]), expansion))
        s += ')'
        s = s[:2 + index] + '(' + s[2 + index:]
    return s

def count_cycle(expansion):
    if '(' in expansion:
        return expansion.index(')') - expansion.index('(') - 1
    else:
        return 0

if __name__ == "__main__":
    d = 0
    longest = 0
    for i in range(1, 1000):
        cycle_length = count_cycle(pretty_format(i))
        if cycle_length > longest:
            d = i
            longest = cycle_length
    print(d)
