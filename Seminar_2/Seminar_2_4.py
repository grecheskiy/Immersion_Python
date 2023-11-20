import math
import decimal

decimal.getcontext().prec = 50
PI = decimal.Decimal(math.pi)

d = decimal.Decimal(input('Enter diameter of the circle: '))
while d > 1000:
    print('Uncorrected enter!')
    d = decimal.Decimal(input('Enter diameter of the circle: '))
print(f'Area of the circle = {PI * (d / 2) ** 2}\nLength of the circle = {PI * d}')
