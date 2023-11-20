a = float(input('Enter a = '))
b = float(input('Enter b = '))
c = float(input('Enter c = '))

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = f'Two roots: {x1=}, {x2=}'
elif d == 0:
    x = -b / (2 * a)
    result = f'One root: {x=}'
else:
    d = complex(d, 0)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = (f'Two complex roots: x1 = {round(x1.real, 2) + round(x1.imag, 2) * 1j}, '
              f'x2 = {round(x2.real, 2) + round(x2.imag, 2) * 1j}')
print(result)
