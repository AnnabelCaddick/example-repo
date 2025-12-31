original_string = input("Write a sentence:")
original_string_with_cap = ""


for i, char in enumerate(original_string):
    if i % 2 == 0:
        original_string_with_cap += char.upper()
    else:
        original_string_with_cap += char.lower()
    
print (original_string_with_cap)


string_2 = input("Write a different sentence here:")

string_2_split = string_2.split()

string_2_split =[
     word.upper() if i %2 == 0 else word.lower()
     for i, word in enumerate(string_2_split)
]

result = " ".join(string_2_split)

print(result)




