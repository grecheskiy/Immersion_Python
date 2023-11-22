data = (42, 73, 3.14, 'Hello world', None, True, 'Text', 100500.2, False)

my_dict = {}
for item in data:
    key = my_dict.setdefault(type(item), [])
    key.append(item)

print(f'{my_dict}')
