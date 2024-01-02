# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import random as rnd

_MIN_VALUE: int = -1000
_MAX_VALUE: int = 1000
_DELIMITER: str = "|"


def fill_file_num(file_name: str, str_count: int):
    """Заполнение файла случайными числами

    :file_name: Имя файла для сохранения.
    :str_count: Кол-во генерируемых пар значений.
    """
    with open(file_name, "a", encoding="UTF-8") as f:
        for _ in range(str_count):
            number_1 = rnd.randint(_MIN_VALUE, _MAX_VALUE)
            number_2 = rnd.uniform(_MIN_VALUE, _MAX_VALUE)
            f.write(f"{number_1}{_DELIMITER}{number_2}\n")
