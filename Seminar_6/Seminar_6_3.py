# Улучшаем задачу 2
# Добавьте возможность запуска функции "угадайки" из модуля в коммандной строке терминала
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение

from sys import argv
from Seminar_6_2 import *

if __name__ == '__main__':
    params = argv[1:]
    print(guess(*(int(param) for param in params)))
