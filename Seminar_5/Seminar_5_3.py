# Продолжаем развивать задачу 2
# Возьмите словарь, который вы получили. Сохраните его итераторатор
# Далее выведите первые пять пар ключ-значение, обращаясь к итератору, а не к словарю

COUNT = 5

text = "Создайте из строки словарь, где ключ - буква, а значение - код буквы."
my_dict = {symbol: ord(symbol) for symbol in set(text)}
my_dict_iter = iter(my_dict.items())

for _ in range(COUNT):
    print(*next(my_dict_iter))
# print(my_dict)
