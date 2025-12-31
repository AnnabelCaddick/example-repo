import statistics
numbers = []
print ("Please input 10 numbers")
for i in range (10):
    number = float(input(f"Enter a number {i + 1}:"))
    numbers.append(number)
print("You entered:", numbers)

numbers_sum = sum(numbers)
print("The total of all the numbers is:", numbers_sum)


max_number = max(numbers)
print("The largest number you entered was :", max_number)
index_of_max_number = numbers.index(max_number)
print("The index of the largest number you entered is:", index_of_max_number)
min_number = min(numbers)
print("The smallest number you entered was:", min_number)
index_of_min_number = numbers.index(min_number)
print("The index of the smallest number you entered is:" , index_of_min_number)
numbers_mean = statistics.mean(numbers)
print(f"The mean average of the numbers you have entered is:, {numbers_mean :.2f}")

numbers_median = statistics.median(numbers)
print(f"The median average of the numbers you have entered is: , {numbers_median:.2f}")