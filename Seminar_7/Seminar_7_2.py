# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import random as rnd


_VOWELS = "AEIOUY"
_CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZ"
_MIN_LEN = 4
_MAX_LEN = 7


def fill_file_name(file_name: str, name_count: int):
    """Заполнение файла случайными именами

    :file_name: Имя файла для сохранения.
    :name_count: Кол-во генерируемых имен.
    """
    names = []
    for _ in range(name_count):
        len_name = rnd.randint(_MIN_LEN, _MAX_LEN)
        name = ""
        for i in range(len_name):
            if i % 3 != 0:
                name += _get_char(_CONSONANTS)
            else:
                name += _get_char(_VOWELS)
        names.append(name)
    with open(file_name, "w", encoding="UTF-8") as f:
        f.writelines('\n'.join(names))


def _get_char(string: str) -> str:
    """Получить символ"""
    pos = rnd.randint(0, len(string) - 1)
    return string[pos]
