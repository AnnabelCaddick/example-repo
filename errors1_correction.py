# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #Syntax error: Missing parentheses around the string.
print ("\n") #Syntax error: Missing parentheses around the string as well as unexpected indent
 # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" # Syntax error with unexpected indent, corrected '==' to '=' as this opperator is for comparison not assignment. "24 years old" cannot be converted into an interger, therefore text part removed.
age = int (age_Str.split()[0])# This line orginally gave a runtime error because python cannot convert the entire string to an interger because it contains non-numeric characters. The corrected version uses .split() to split the string up and [0] takes the "24"
print(f"I'm {age} years old.") # Runtime error because you cannot add a string and interger together, an f string is added to correct the problem.

# Variables declaring additional years and printing the total years of age
years_from_now = 3 #To fix the logical error the "" were removed to convert the 3 from a string into an interger so it can be added to the age variable. To fix the syntax error, the unexpected indent was also removed to ensure the code could run.
total_years = age + years_from_now 

print (f"In three years from now I will be: {total_years} years old") #The print statement was converted into an f' string so that the value of the selected variables can be put directly inside a string. The correct variable name was also added. The contents of the string was also adjusted to make the results of the code make sense.

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total_years * 12 #Logical error. The variable name corrected from 'total' to 'total_years'
print (f"In 3 years and 6 months I will be: {total_months + 6} months old.") #Syntax error, to fix this parentheses added and the print statement was converted into an f-string'. 6 was added to the total months to make the statement correct.

#HINT, 330 months is the correct answer

 
