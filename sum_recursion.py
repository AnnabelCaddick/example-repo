#Get the user to enter as many numbers as they want and then put these numbers into a list when
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


user_index = input(f"Please enter an index number (0 to {len(numbers)-1}:")



try:
    index = int(user_index)
    
    if 0 <= index < len(numbers):
        print(f"Value at index is: {numbers[index]}")
        
    else:
        print("Index out of range.")

except ValueError:
    print("Invalid index.")

def get_elements(numbers, index):
    return numbers[index]



def sum_up_to_index(numbers, index):
    return sum(numbers[:index + 1])

result = sum_up_to_index(numbers, index)
print(f" The result of the sum of the numbers in the list up to and including the index is: {result}")

def sum_up_to_index(numbers, index):
    if index < 0 or index >= len(numbers):
        raise IndexError("Index out of range.")

    if index == 0:
        return numbers [0]

    return numbers[index] + sum_up_to_index(numbers, index - 1)
    print(f"The sum of the numbers up to and including the index is: {sum_up_to_index(numbers, index)}")
