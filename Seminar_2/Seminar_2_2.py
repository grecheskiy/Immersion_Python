import sys
data = [42, 73.0, 'Hello world', True, 42, 'Hello world', 256, 2 ** 8, 'Hello world']

for nn, value in enumerate(data, 1):
    check_int = 'Like whole number' if isinstance(value, int) else ''
    check_str = 'Like line' if isinstance(value, str) else ''
    print(f'{nn}. Object {value}.\nAddress in memory {id(value)}.\tSize in memory {sys.getsizeof(value)}.'
          f'\tHash object {hash(value)}.\t{check_int}{check_str}')
