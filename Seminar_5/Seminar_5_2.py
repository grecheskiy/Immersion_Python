# Самостоятельно сохраните в переменной строку текста
# Создайте из строки словарь, где ключ - буква, а значение - код буквы
# Напишите преобразование в одну строку

text = "Создайте из строки словарь, где ключ - буква, а значение - код буквы."
my_dict = {symbol: ord(symbol) for symbol in set(text)}
print(my_dict)
