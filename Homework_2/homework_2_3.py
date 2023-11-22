from fractions import Fraction

#str_1 = "10/11"
#str_2 = "20/22"
#num_1 = str_1.split("/")
#num_2 = str_2.split("/")
#a = num_1[0]
#b = num_1[1]
#c = num_2[0]
#d = num_2[1]
#result = a + b
#print(f'{result}')

first_fract = input('Введите первую дробь формата "a/b": ').split('/')
second_fract = input('Введите вторую дробь формата "a/b": ').split('/')

fract_1 = int(first_fract[0]) / int(first_fract[1])
fract_2 = int(second_fract[0]) / int(second_fract[1])
pro_fract_1 = Fraction(int(first_fract[0]), int(first_fract[1]))
pro_fract_2 = Fraction(int(second_fract[0]), int(second_fract[1]))

print(f'Сумма дробей: {fract_1 + fract_2}')
print(f'Проверка: {pro_fract_1 + pro_fract_2}')

print(f'Произведение дробей: {fract_1 * fract_2}')
print(f'Проверка: {pro_fract_1 * pro_fract_2}')

