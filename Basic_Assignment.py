def add(x, y):
    print("Result = ", x+y)

def sub(x, y):
    print("Result = ", x-y)

def mult(x, y):
    print("Result = ", x*y)

def div(x, y):
    if y == 0:
        print("Division not possible.")
    else:
        print("Result = ", x/y)

print("______CALCULATOR_____")
i='Y'
while (i=='Y' or i=='y'):    
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")
    choice = input("Enter your choice: ")
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    if choice == '1':
        add(n1, n2)
    elif choice == '2':
        sub(n1, n2)
    elif choice == '3':
        mult(n1, n2)
    elif choice == '4':
        div(n1, n2)
    else:
        print("Wrong Choice :(")
    print("Do you want to restart calculator?")
    i = input("YES- press y/Y or NO- press n/N :")


