# Python Program - Make Simple Calculator

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
while True:
    choice = None
    choice = int(input("Which function? "))
    if (choice>=1 and choice<=4):
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        if choice == 1:
            res = num1 + num2
            print("Result = ", res)
        elif choice == 2:
            res = num1 - num2
            print("Result = ", res)
        elif choice == 3:
            res = num1 * num2
            print("Result = ", res)
        else:
            res = num1 / num2
            print("Result = ", res)
    elif choice == 5:
        exit()
    else:
        print("Wrong input..!!")
