numbers = []
print("Enter a list of numbers and type done when you are finished.")

while True:
    user_list_num = input("Enter a number or type done to finish:")

    if user_list_num.lower() == "done" :
        print ("You have finished your list.")
        break

    try:
        list_number = float(user_list_num)  
    except ValueError:
        print("Please enter a valid number.")
        continue

    numbers.append(list_number)

print(f"Your list of numbers is" , numbers)

def largest_number(numbers, index):

    if index == 0:
        return numbers [0]

    largest_so_far = largest_number(numbers, index -1)

    if numbers[index] > largest_so_far:
        return numbers[index]
    else:
        return largest_so_far
    
print(f"The largest number in your list is: {largest_number(numbers, len(numbers) - 1)}")