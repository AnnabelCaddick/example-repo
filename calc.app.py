
print("This is a simple calculator application. \n"
     "The application will allow you to add, subtract, multiply or divide any two numbers of your choice.")

while True:
    try:
        num1 = float(input("Please enter your first number:"))
        num2 = float(input("Please enter your second number:"))
        break
    except ValueError:
        print("That was not a valid entry. Please try again.")

operator = input("Please enter an operator (+, -, *, /):")

result = None
try:

    if operator == "+":
         result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    else:
        print ("Invalid operator")

except ZeroDivisionError:
    print("You cannot divide by zero.")

if result is not None:
    try: 
        with open('equations.txt' , 'a') as file:
            file.write(f"{num1} {operator} {num2} = {result:.2f}\n")
        print("The result has been saved into equations.txt")
    except Exception as e:
        print("Error saving calculation:", e)
    
full_list = input("Would you like to print all the calculations you have previously entered? ENTER YES OR NO")

if full_list.lower() == "yes":
    try:
        with open ("equations.txt", "r") as file:
          print ("\n ### ALL STORED CALCULATIONS ###")
          print(file.read())
    except FileNotFoundError:
        print ("No calculations have been stored yet.")

         