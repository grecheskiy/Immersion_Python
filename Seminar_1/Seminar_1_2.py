LOWER_LIMIT = 1
UPPER_LIMIT = 999
ONE = 1
TEN = 10
HUNDRED = 100
SQUARE = 2

num = LOWER_LIMIT
while num < LOWER_LIMIT or UPPER_LIMIT:
    num = int(input(f'Enter number from {LOWER_LIMIT} till {UPPER_LIMIT}'))
if num < TEN:
    res = f'Number {num} number. It square = {num**SQUARE}'
elif num < HUNDRED:
    first_num = num//TEN
    second_num = num%TEN
    res = f'Number {num} - too numbers. multiple numbers = {first_num*second_num}'
else:
    first_num = num//HUNDRED
    second_num = num//TEN%TEN
    third_num = num%TEN
    mirror = third_num * HUNDRED + second_num * TEN + first_num
    res = f'Number {num} - free numbers. it mirror number = {mirror}'
print(res)
