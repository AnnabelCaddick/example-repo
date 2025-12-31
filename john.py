incorrect_names = []
while True:
    user_input = input("Please enter your name:")
    if user_input.lower() =="john":
      print ("You have ended the loop by entering 'john.")
      break 
    
    incorrect_names.append(user_input)
print (f"The incorrect names entered were: {incorrect_names}" )