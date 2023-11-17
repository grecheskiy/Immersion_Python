a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("The triangle does not exist")
elif a != b and b != c and a != c:
    print("The triangle is versatile")
else:
    print('The triangle is equilateral or isosceles')
