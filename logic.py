#This code has a logical error.
#The number of rows is not right for the desired pattern.
#The code runs and produces a pattern.
#For the correct pattern to run the number of rows should be '9' not '90'.
rows = 90
for i in range (1, rows +1):
    if i <= 5:
        stars = i 
   
    elif i <= 8:
        stars = 10 - i
    
    else:
        stars = 1
    print("*" * stars)
