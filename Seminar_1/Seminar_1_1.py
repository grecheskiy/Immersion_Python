REFORM = 1582
BIG_LEAP_YEAR = 400
SMALL_LEAP_YEAR = 4
LARGE_NON_LEAP_YEAR = 100
MULTIPLE = 0

year = int(input("Enter year "))
if year < REFORM:
    res = "error"
elif year % BIG_LEAP_YEAR == MULTIPLE:
    res = f'{year} - correct'
elif year % LARGE_NON_LEAP_YEAR == MULTIPLE:
    res = f'{year} - not correct'
elif year % SMALL_LEAP_YEAR == MULTIPLE:
    res = f'{year} - correct'
else:
    res = f'{year} - not correct'
print(res)
