#def to_hex(num):
#   hex_str = hex(num)[2:].upper()
#    return hex_str

#num = int(input("Введите целое число: "))
#hex_string = to_hex(num)
#print(f"Число в шестнадцатиричном представлении: {hex_string}")
#print("Проверка результата функцией hex", hex(num))

BIN = 2
OCT = 8
HEX = 16

num = int(input('Enter integer number: '))

for div in (BIN, OCT, HEX):
    result: str = ''
    test_num: int = num
    while test_num > 0:
        result = str(test_num % div) + result
        test_num //= div

    print(f'For {div=} {result=}')
print(f'binary number {bin(num)}, octal number {oct(num)}, hex number {hex(num)}')
