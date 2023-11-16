SPACE = ''
STAR = '*'
ONE = 1
rows = int(input('Enter number stars: '))
spaces = rows - ONE
stars = ONE
for i in range(rows):
    print(spaces * stars * STAR)
    spaces += ONE
    stars += ONE + ONE
