data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]

new_data = []
for nn, item in enumerate(data, 1):
    if item % 2 != 0:
        new_data.append(nn)

print(f'{data = }\n{new_data = }')

