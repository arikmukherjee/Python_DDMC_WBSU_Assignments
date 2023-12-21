#add two numbers
def add(num1,num2):
    result=num1 + num2
    return result
#subtract two numbers
def subtract(num1,num2):
    result=num1 - num2
    return result
#multiply two numbers
def multiply(num1,num2):
    result=num1 * num2
    return result
#devide two numbers
def devide(num1,num2):
    result=num1 / num2
    return result
#Menu for user
print("---WELCOME---")
print("1. Press 1 to add")
print("2. Press 2 to subtract")
print("3. Press 3 to multiply")
print("4. Press 4 to devide")
#Taking input from user to perform any operation
choice=int(input("Enter your choice:1/2/3/4 \n"))
#Taking two numbers numbers for operation
first_number=int(input("Enter first number"))
second_number=int(input("Enter second number"))

if choice == 1:
    print(first_number, "+", second_number, "=",add(first_number,second_number)) 
elif choice == 2:
    print(first_number, "-", second_number, "=",subtract(first_number,second_number))
elif choice == 3:
    print(first_number, "*", second_number, "=",multiply(first_number,second_number))
elif choice == 4:
    print(first_number, "/", second_number, "=",devide(first_number,second_number))
else:
    print("Invalid input")