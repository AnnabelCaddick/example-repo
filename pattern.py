

total_lines = 9
for i in range (1, total_lines +1):
    if i <= 5:
        stars = i

    elif i <= 8:
        stars = 10 - i
    
    else: 
        stars = 2
    print ("*" * stars)