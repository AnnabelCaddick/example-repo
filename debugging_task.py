# Function to print dictionary values given the keys
#Change the k to key
#remove . on like 5
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) 

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!",    #Changed the '' to ""
                         "maggie": "(Pacifier Suck)"
                         }
#create a for loop
#correct print_values_of to print on line 18
for name in ["lisa", "bart", "homer"]:
    print(simpson_catch_phrases[name])



'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''


