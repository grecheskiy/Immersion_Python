# Создайте модуль с функцией внутри
# Функция получает на вход загадку, список с возможными вариантами отгадок и кол-во попыток на угадывание
# Порграмма возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны

def riddle(riddle_text: str, answer: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку:\n{riddle_text}')
    for nn in range(1, count +1):
        ans = input(f'Попытка №{nn}: ').lower()
        if ans in answer:
            return nn
    return 0


if __name__ == '__main__':
    result = riddle('Зимой летом одним цветом', ['ель', 'ёлка', 'елка', 'сосна'])
    print(f'Угодал с {result}й попытки' if result > 0 else 'Не угадал!')
