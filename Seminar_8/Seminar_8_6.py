# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текс загадки)
# и число (номер попытки, с которой она угадана)
# Функция формирует словарь с информацией о результатах отгадывания
# Для хранения используйте защищенный словарь уровня модуля
# Отдельно напишите функцию, которая выводит результаты угадывания из защищенного словаряв удобном для чтения виде
# Для формирования результатов используйте генераторное выражение

_data = {}


def riddle(riddle_text: str, answer: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку:\n{riddle_text}')
    for nn in range(1, count +1):
        ans = input(f'Попытка №{nn}: ').lower()
        if ans in answer:
            return nn
    return 0


def save_results(puzzle: str, nn: int) -> None:
    _data[puzzle] = nn


def show_results():
    res = (f'Загадку "{puzzle}" разгодали с {nn}й попытки' if nn > 0
           else f'Загадку "{puzzle}" не разгодали'
           for puzzle, nn in _data.items())
    print(*res, sep='\n')


def storage():
    puzzles = {
        'Зимой летом одним цветом': ['ель', 'ёлка', 'елка', 'сосна'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
        'Не лает, не кусает, в дом не пускает': ['замок', 'домофон'],
    }
    for puzzle, answers in puzzles.items():
        result = riddle(puzzle, answers)
        print(f'Угодал с {result}й попытки' if result > 0 else 'Не угадал!')
        save_results(puzzle, result)


if __name__ == '__main__':
    storage()
    show_results()
