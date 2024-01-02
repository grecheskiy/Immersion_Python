# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.
def fill_num_names_file(num_file: str, name_file: str, destination: str):
    """Генерация нового файла их файлов имен и цифр

    :num_file: Файл с цифрами.
    :name_file: Файл с именами.
    :destination: Результирующий файл.
    """
    with (
        open(num_file, "r", encoding="UTF-8") as f_num,
        open(name_file, "r", encoding="UTF-8") as f_name,
    ):
        list_num = [int(n[0]) * float(n[1]) for n in map(lambda x: x.split(_DELIMITER), list(f_num))]
        list_names = [s.replace("\n", '') for s in list(f_name)]
    # формирование нового списка значений
    count_names = len(list_names)
    count_nums = len(list_num)
    count_new_item = max(count_nums, count_names)
    num_pos = name_pos = 0
    new_list = []
    for _ in range(count_new_item):
        if list_num[num_pos] < 0:
            new_list.append(f"{list_names[name_pos].lower()} - {abs(list_num[num_pos])}")
        else:
            new_list.append(f"{list_names[name_pos]} - {round(list_num[num_pos])}")
        num_pos += 1
        name_pos += 1
        if num_pos == count_nums:
            num_pos = 0
        if name_pos == count_names:
            name_pos = 0
    # Запись нового списка в файл
    with open(destination, "w", encoding="UTF-8") as f_new:
        f_new.writelines('\n'.join(new_list))