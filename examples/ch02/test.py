number1 = int(input("Enter the fist number"))
number2 = int(input("Enter the second number"))
number3 = int(input("Enter the third number"))


minimum = number1

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

print("Minimum value is ",minimum)