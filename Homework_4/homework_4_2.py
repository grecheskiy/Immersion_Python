def string_to_dict(text: str) -> dict[str, int]:
    num1, num2 = map(int, text.split())
    if num1 > num2:
        num1, num2 = num2, num1
    result = {}
    for i in range(num1, num2 + 1):
        result[chr(i)] = i
    return result


print(string_to_dict("90 97"))
print(string_to_dict("87 80"))
