# Функция получает на вход строку из двух чисел через пробел
# Сформируйте словарь, где ключем будет символ из Unicode, а значением целое число
# Диапозон пар ключ-значение от наименьшего из введенных пользователем чисел до нибольшего включительно

def range_unicode(text: str) -> dict[str, int]:
    first, second = map(int, text.split())
    result = {}
    for number in range(min(first, second), max(first, second) + 1):
        result[chr(number)] = number
    return result

print(range_unicode('4321 4331'))
