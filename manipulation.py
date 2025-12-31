str_manip = input("Please write a sentence")
print("The number of characters in your sentence is:" , len(str_manip))
last_letter = str_manip [-1]
print("The last letter in your sentence is:" + last_letter)
new_sentence = str_manip.replace(last_letter, "@")
print(new_sentence)
last_three_letters_reversed = str_manip [-3:][::-1]
print(last_three_letters_reversed)
first_three_letters = (str_manip [:4])
print("The first three letters of your sentence are :" , first_three_letters)
last_two_letters = (str_manip [-2:])
print (" The last two letters of the sentence are :" , last_two_letters)
new_five_word = first_three_letters + last_two_letters
print("The new word made up of the first three and last two letters is:" , new_five_word)

