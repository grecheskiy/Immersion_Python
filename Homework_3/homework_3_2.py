list_1 = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9]

new_list_1 = list(set(list_1))

r_list_1 = []
for item in list_1:
    if list_1.count(item) > 1:
        r_list_1.append(item)

print(f'original: {list_1}\nсписок без повторов: {new_list_1}\nсписок повторов: {r_list_1}')