import random
joke_list = [
             ("Why don't skeletons fight each other?\nANSWER: They don't have guts!"), 
             ("What do you call cheese that is not yours?\nANSWER: Nacho Cheese!"), 
             ("Why did the maths book look sad?\nANSWER: Because it had too many problems!"),
             ("Why did the tomato turn red?\nANSWER: Because it saw the salad dressing! "), 
             ("What do you call a fake noodle?\nANSWER: An impasta!")]
for joke in joke_list:
    print(joke)

print ("###This code will now produce a random joke using the random function in python###")
random_joke = random.choice(joke_list)
print(random_joke)