# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# Assume 1 Jan 1900 was a Monday

def is_leap_year(n):
    if n % 4 != 0:      # leap years on years divisible by 4
        return False
    if n % 400 == 0:    # also on years divisible by 400 
        return True
    if n % 100 == 0:    # but not other centuries
        return False
    return True

#                 1   2   3   4   5   6   7   8   9   10  11  12
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#            0      1      2       3      4        5      6
weekdays = ["sun", "mon", "tues", "wed", "thurs", "fri", "sat"]

def cal_gen(y, m, d, wkdy):
    year = y
    month = m
    day = d
    wkday = wkdy
    while True:
        yield (year, month, day, wkday)
        if ((day < 31 and month in (1, 3, 5, 7, 8, 10, 12)) or
           (day < 30 and month in (4, 6, 9, 11)) or
           (day < 28 and month == 2) or
           (day < 29 and month == 2 and is_leap_year(year))):
               day += 1
        elif month < 12:
            month += 1
            day = 1
        else:
            year += 1
            month = 1
            day = 1
        wkday = (wkday + 1) % 7


if __name__ == "__main__":
    first_of_month_sunday = 0
    cal = cal_gen(1900, 1, 1, 1)
    date = next(cal)
    while date[0] < 2001:
        if (date[0] > 1900 and
            date[2] == 1 and
            date[3] == 0):
            first_of_month_sunday += 1
        date = next(cal)

    print(first_of_month_sunday)
