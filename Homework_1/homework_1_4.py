from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT_COUNT = 10

hidden_number = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 1
while count <= ATTEMPT_COUNT:
    print(f"Attempt {count}. Enter an integer number: ")
    entered_number = int(input())

    if entered_number == hidden_number:
        print("YOU WIN!!!")
        break
    elif hidden_number < entered_number:
        print("less")
    elif hidden_number > entered_number:
        print("more")

    count += 1

else:
    print("YOU LOSE!!!")


