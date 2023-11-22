data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
new_data = list(set(data))

new_list = []
for item in data:
    if item not in new_list:
        new_list.append(item)

print(f'original: {data}\nno repetitions new_data: {new_data}\nno repetitions new_list: {new_list}')
