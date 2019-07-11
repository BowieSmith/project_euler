# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

def read_names(names_file):
    names = []
    with open(names_file) as f:
        for line in f:
            names.extend(line.split(','))
    return names

def letter_value(letter):
    return ord(letter) - 64

def name_value(name):
    return sum(letter_value(l) for l in name)

if __name__ == "__main__":
    names = read_names("../p022_names.txt")
    names = [n.strip('"') for n in names]
    names.sort()
    total = sum((name_value(name) * (position + 1)) for position, name in enumerate(names))
    print(total)
