LOWER_LIMIT = 0
UPPER_LIMIT = 100000

num = float(input(f'Enter number from {LOWER_LIMIT} till {UPPER_LIMIT} \n'))

if num < 0 or num > 100000:
    print("ERROR")
elif num // num == 1 and num // 1 == num:
    print("The number is simple")
else:
    print("The number is composite")
