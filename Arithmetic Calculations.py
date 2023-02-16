num1 = int(input("Enter any number:"))
num2 = int(input("Enter another number:"))
print("Arithmetic Operations to be performed:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
n = int(input('How many times would you like to perform the arithmetic operations? '))
while n:
    op = int(input('Which operation would you like to perform? '))
    if op == 1:
        add = num1 + num2
        print(num1, " + ", num2, " = ", add)
        print("Sum of ", num1, " and ", num2, " is ", add)
        n = n - 1
    elif op == 2:
        dif = num1 - num2
        print(num1, " - ", num2, " = ", dif)
        print("Difference of ", num1, " and ", num2, " is ", dif)
        n = n - 1
    elif op == 3:
        prod = num1 * num2
        print(num1, " * ", num2, " = ", prod)
        print("Product of ", num1, " and ", num2, " is ", prod)
        n = n - 1
    elif op == 4:
        div = num1 / num2
        print(num1, " / ", num2, " = ", div)
        print("Quotient of ", num1, " and ", num2, " is ", div)
        n = n - 1
    elif op == 5:
        print("Thank You!")
        n = 0
    else:
        print("Invalid Choice")
        n = n - 1
