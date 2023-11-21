from fractions import Fraction

a = int(input("Enter a= "))
b = int(input("Enter b= "))

print(Fraction(a, b))

# ввод числителей и знаменателей двух дробей
a = int(input("Введите числитель первой дроби: "))
b = int(input("Введите знаменатель первой дроби: "))
c = int(input("Введите числитель второй дроби: "))
d = int(input("Введите знаменатель второй дроби: "))

# нахождение произведения дробей
numerator = a * c
denominator = b * d

# сокращение дроби
def gcd(a, b):
if b == 0:
return a
else:
return gcd(b, a % b)

divisor = gcd(numerator, denominator)
numerator //= divisor
denominator //= divisor

# вывод результата
print("Произведение дробей равно:", numerator, "/", denominator)