# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #Syntax error missing quotation marks.
animal_type = "cub"
number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth.") #f' string missing to allow for the selected variavles to be added directly into the string. Parentheses also added. The location of the variables 'number_of_teeth' and 'animal_type' were swapped round to fix a logical arror to ensure the string made sense.

print (full_spec) #Parentheses added