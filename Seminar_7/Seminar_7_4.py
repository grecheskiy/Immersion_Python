# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
import random as rnd


def create_file_with_ext(extension: str, /, min_len: int = 6, max_len: int = 30, min_rand_bytes: int = 256,
                         max_rand_bytes: int = 4096, count_files: int = 42):
    for _ in range(count_files):
        file_name = set()
        for _ in range(rnd.randint(min_len, max_len)):
            file_name.add(chr(rnd.randint(ord('a'), ord('z'))))

        full_name = ''.join(file_name) + "." + extension
        with open(full_name, "bw") as file:
            file.write(bytes(rnd.randint(0, 255) for _ in range(rnd.randint(min_rand_bytes, max_rand_bytes))))