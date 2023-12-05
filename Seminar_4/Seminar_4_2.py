# Функция, принимает строку текста
# Список с уникальными кодами Unicode каждого символа введенной строки отсортированный по убыванию

def uni_list(text: str) -> list[int]:
    result = []
    for symbol in set(text):
        result.append(ord(symbol))
    return sorted(result, reverse=True)

print(uni_list('каждый охотник желает знать, где сидит фазан'))
