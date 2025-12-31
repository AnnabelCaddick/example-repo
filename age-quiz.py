age = int(input("How old are you?"))
print("Your age is" , age)
if age > 100:
    print("Sorry you are dead!")
elif 40 <= age <65:
    print ("You are over the hill!")
elif 65 <= age <= 100:
    print("Enjoy retirement!")
elif age < 13:
    print ("You qualify for the kiddie discount!")
elif age == 21:
     print ("Congrats on your twenty first!")
else:
    print ("Age is but a number!")
     