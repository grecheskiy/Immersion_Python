# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10) человек в качестве значения
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные.
# верните истину, а если хотя бы одна убыточная - ложь
def my_lamda(cur_list):
    return sum(cur_list) > 0


def final_income(my_dict: dict[str, list[int | float]]) -> bool:
    return all(map(lambda cur_list: sum(cur_list) > 0, my_dict.values()))
#    return all(sum(cur_list) > 0 for cur_list in my_dict.values())


data = {
    "Ecco": [42, -73, 12, 85, -15, 2],
    "Adidas": [45, 25, -100, 22, 1],
    "Rebook": [-500, 123, 52, 45, 93]
}
print(final_income(data))
