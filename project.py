'''
write a program to print calculator?
'''
def add(x, y):
    return x+y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def power(x,y):
    return x**y
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5.power")
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice in ['1', '2', '3', '4','5']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1}**{num2}={power(num1,num2)}")


        except ValueError:
            print("Invalid input! Please enter numerical values.")
    else:
        print("Invalid choice! Please select a valid operation.")
calculator()
'''
output:-
1. Add
2. Subtract
3. Multiply
4. Divide
5.power
Enter choice (1/2/3/4/5): 1
Enter first number: 6
Enter second number: 7
6.0 + 7.0 = 13.0
1. Add
2. Subtract
3. Multiply
4. Divide
5.power
Enter choice (1/2/3/4/5): 2
Enter first number: 67
Enter second number: 54
67.0 - 54.0 = 13.0
1. Add
2. Subtract
3. Multiply
4. Divide
5.power
Enter choice (1/2/3/4/5): 3
Enter first number: 5
Enter second number: 6
5.0 * 6.0 = 30.0
1. Add
2. Subtract
3. Multiply
4. Divide
5.power
Enter choice (1/2/3/4/5): 4
Enter first number: 49
Enter second number: 7
49.0 / 7.0 = 7.0
1. Add
2. Subtract
3. Multiply
4. Divide
5.power
Enter choice (1/2/3/4/5): 5
Enter first number: 3
Enter second number: 4
3.0**4.0=81.0
