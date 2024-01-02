# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
def gen_files(extensions: list[str]):
    for e in extensions:
        create_file_with_ext(e, count_files=1)


if __name__ == "__main__":
    fill_file_num("numeric.txt", 10)
    fill_file_name("names.txt", 10)
    fill_num_names_file("numeric.txt", "names.txt", "new.txt")
    create_file_with_ext("txt", count_files=5)