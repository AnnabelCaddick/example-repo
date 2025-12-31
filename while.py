#Ask user to continually enter a number
#When the user enters -1 stop requesting they enter numbers
# 0 is not a valid input
# think how you would exit the loop if -1 was entered
#the program entered must calculate the average of the valid nubers entered including -1 and 0
#Use a while loop to achieve the continuous prompting and number collection.
print ("Please follow the instructions and enter a number when instructed to do so.")
print ("If you want to finishing entering numbers please type 'done' or '-1'.")
print ("Once you have done this the program will print out the average of the numbers you have entered.")
sum_of_user_numbers = 0
count = 0
while True: 
    user_input = input("Enter a number:")
    if user_input.lower() in ("done", "-1"):
        print ("You have chosen to end the loop by entering either 'done' or '-1'.")

        break

    try:
        number = float(user_input)
        sum_of_user_numbers += number
        count += 1
    except ValueError: 
        print ("Please enter a valid number")

if count > 0:
    average_of_inputed_numbers = sum_of_user_numbers / count
    print(f" The average of the numbers entered is: {average_of_inputed_numbers}")

else:
    print ("Invalid input try again.")