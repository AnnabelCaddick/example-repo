#Import the math module to access to the maths module and mathematical functions. 
#print a string explaing the meaning of investment and bond.
#Create the variable 'interest' but leave the value unset.
#Get the user to input either bond or investment.
#Use the function .strip() to remove extra spaces.
#Use the lower() function to make the input case-insensitive.
import math 
print("Investment - To calculate the amount of interest you will earn on your investment." ) 
print ("Bond - To calculate the amount you will have to pay on a home loan.") 
print("Please enter either 'investment' or 'bond' onto the line below: ") 
interest = None 
bond_or_investment = (input("Enter Bond or Investment: ").strip().lower()) 



#If the user chose investment, run the investment calculation section.
#Create the deposit variable.
#Convert the user's input into a float (a decimal number).
#Ask the user how much money they will be depositing.
#Create the percentage_interest_rate variable.
#Convert the user's input into a float (a decimal number).
#Ask the user to input their percentage intrest rate.
#Create the years_investing variable. 
#Convert the user's input into an interger (a whole number).
#Ask the user to input how many years they are planning to invest for.
#Ask the user to input either 'compound' or 'simple' and enter their input into the variable 'interest'.
# Use .strip() to remove extra spaces and lower() to make the input case-insensitive.
if   bond_or_investment =="investment": 
    deposit = float(input("How much money will you be depositing in pounds (£)?")) 
    percentage_interest_rate = float(input("Enter your percentage interest rate (%): ")) 
    years_investing = int(input("How many years are planning to invest for?: ")) 
    interest = input(" Do you want simple or compound interest? Please enter either simple or compound: ").strip().lower() 



#If the user inputted 'simple', run the simple interest calculation.
#Calculate interest rate as a decimal, convert the answer into a float.
#Create a variable called rate and input the answer into the rate variable.
#Create a variable called total_amount_with_simple_interest.
#Calculate the simple interest using the relevant variables and input the answer into the the variable total_amount_with_simple_interest.
#Print variable 'total_amount_with_simple_interest'.
#Use :.2f to format the number as a float with 2 decimal places.
#Create a variable called simple_interest_earned.
#Calculate the simple interest earned using the relevant variables and store the result in the variable called simple_interest_earned.
#Use 'f' at the start to turn the string into an f-string to allow variables to be inserted inside the text.
#Print variable 'simple_interest_earned'.
#Use :.2f to format the number as a float with 2 decimal places.
    if interest == "simple": 
       rate = float(percentage_interest_rate/100) 
       total_amount_with_simple_interest = deposit * (1+ rate * years_investing) 
       print (f"Your total amount in pounds (£) when simple interest is applied is : £{total_amount_with_simple_interest:.2f}") #The 'f' at the start turns this into an f-string to allow variables to be inserted inside the text.
       simple_intrest_earned = total_amount_with_simple_interest - deposit 
       print (f" The simple interest you have earned/ will earn is: £ {simple_intrest_earned:.2f}") 



#If the user selected 'compound' run the compound interest calculation section.
#Calculate interest rate as a decimal, convert the answer into a float.
#Create a variable called total_amount_with_compound_interest.
#Calculate the total amount with compound interest.
#Store the result in the variable called total_amount_with_compound_interest.
#Use 'f' at the start to turn the string into an f-string to allow variables to be inserted inside the text.
#Print variable 'total_amount_with_compound_interest'.
#Use :.2f to format the number as a float with 2 decimal places.
#Create a variable called compound_interest_earned.
#Calculate the compound interest earned using the relevant variables and store the result in the variable called compound_interest_earned.
#Use 'f' at the start to turn the string into an f-string to allow variables to be inserted inside the text.
#Print variable 'compound_interest_earned'.
#Use :.2f to format the number as a float with 2 decimal places.
#If the user enters something other than 'simple' or 'compound' into the input requesting the user inputs 'simple' or 'compound' tell the user that their choice is invalid and ask them to enter either 'simple' or 'compound'.
    elif interest == "compound": 
       rate =float(percentage_interest_rate/100) 
       total_amount_with_compound_interest = deposit * math.pow((1+ rate) , years_investing) 
       print(f"Your total amount in pounds (£) when compound interest is applied is: £{total_amount_with_compound_interest:.2f}") 
       compound_intrest_earned = total_amount_with_compound_interest - deposit 
       print (f" The compound interest you have earned/ will earn is : £ {compound_intrest_earned:.2f}") 
    else:
       print("Invalid type of interest please enter Simple or Compound.") 



#If the user chose 'bond', run the bond calculation section.
#Create the current_house_value variable. 
#Convert the user's input into a float (a decimal number).
#Ask the user to input the value of the house.
#Create the bond_interest_rate variable.
#Convert the user's input into a float (a decimal number).
#Ask the user to input the interest rate on the bond.
#Create a months_for_repayment variable.
#Convert the user's input into a float (a decimal number).
#Ask the user to input how many months they want to repay the bond.
#Create a variable called monthly_interest_rate.
#Use the relevant variables to calculate the users monthly interest rate.
#Store the answer in the monthly_interest_rate variable.
#Create a variable called repayment.
#Calculate the amount the user will have to repay.
#Store the result in the variable 'repayment'
#Use 'f' at the start to turn the string into an f-string to allow variables to be inserted inside the text.
#Print variable 'repayment'.
#Use :.2f to format the number as a float with 2 decimal places.
#If the user enters something other than 'bond' or 'investment' into the input requesting the user inputs 'bond' or 'investment' print string telling user that their choice is invalid and ask them to enter either 'bond' or 'investment'.
elif bond_or_investment == "bond": 
     current_house_value = float((input("What is the present value of the house in pounds (£)? : "))) 
     bond_interest_rate = float((input("What is the interest rate on the bond (%)? : "))) 
     months_for_repayment = float((input("How many months are you planning to take to repay the bond: "))) 
     monthly_interest_rate = float((bond_interest_rate/100)/12) 
     repayment = float((monthly_interest_rate*current_house_value)/(1-(1+ monthly_interest_rate)**(- months_for_repayment))) 
     print(f"The amount you will have to repay each month is: £{repayment:.2f}") 
  
else:
     print("Invalid choice please enter Investment or Bond.") 
