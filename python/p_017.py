# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

num_spelling_dict = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
}

def spelling(n):
    spelling = ''
    if n in num_spelling_dict:
        return num_spelling_dict[n]
    thousands = n // 1000
    if thousands > 0:
        spelling += num_spelling_dict[thousands] + "thousand"
        n = n - ((n // 1000) * 1000)
    hundreds = n // 100
    if hundreds > 0:
        spelling += num_spelling_dict[hundreds] + "hundred"
        n = n - ((n // 100) * 100)
    if (thousands > 0 or hundreds > 0) and n > 0:
        spelling += "and"
    if n in num_spelling_dict:
        spelling += num_spelling_dict[n]
    else:
        tens = n // 10
        if tens > 0:
            spelling += num_spelling_dict[tens * 10]
            n = n - ((n // 10) * 10)
        singles = n % 10
        if singles > 0:
            spelling += num_spelling_dict[singles]
    return spelling

if __name__ == "__main__":
    ans = sum(len(spelling(n)) for n in range(1, 1001))
    print(ans)
