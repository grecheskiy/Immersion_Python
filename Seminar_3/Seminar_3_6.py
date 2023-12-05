data = sorted(input("Введите строку текста: ").split())
print(data)
max_len = 0

for item in data:
    if len(item) > max_len:
        max_len = len(item)

for nn, word in enumerate(data, 1):
    print(f'{nn},  {word:>{max_len}}')
