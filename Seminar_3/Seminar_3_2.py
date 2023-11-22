data = input("Enter the data: ")

if data.isdigit():
    new_data = int(data)
elif data.count('.') == 1 and data.count('-') < 2 and '-' not in data[1:] and \
        data.replace('.', '').replace('-', '').isdigit():
    new_data = float(data)
elif not data.islower():
    new_data = data.lower()
else:
    new_data = data.upper()

print([new_data])


