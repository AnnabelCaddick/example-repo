numbers = [27,-3, 4, 5, 35, 2, 1,-40, 7, 18, 9,-1, 16, 100]

def quick_sort(numbers_list):

#Quick sort is suitable to sort this list because 
#1) Quick sort performs well with small to medium size lists such as this one (14 items).
#2) Quick sort can handle unsorted data with both negative and positive intergers without any additional work. Given this list has no existing order and has both negative and positive intergers quick sort is suitable.
#3) Quick sort has an average time complexity of O(n log n) and sorts the data in place without requiring additional memory.

    if len(numbers_list) <= 1:
        return numbers_list
    pivot = numbers_list[0]
    left = [x for x in numbers_list[1:] if x <= pivot]
    right = [x for x in numbers_list[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

sorted_numbers = quick_sort(numbers)
print("Sorted list:", sorted_numbers)

def binary_search(numbers_list, target):

    low = 0
    high = len(numbers_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers_list[mid] == target:
            return mid
        elif numbers_list[mid] < target:
                low = mid + 1
        else: 
                high = mid - 1
    return -1
target = 9
index = binary_search(sorted_numbers, target)

if index != -1:
    print(f"Number {target} found at index: {index}")

else:
    print(f"Number {target} not found in the list")


#Insertion sort builds the sorted element one element at a time. for each element, it compares the element before it and inserts it into the corrct position. It is efficent for very small lists or lists that have nearly been sorted.


def insertion_sort(numbers_list):
#Sorts a list in ascending order using insertion sort.

for i in range(1, len(numbers_list)):
    key = numbers_list[i]
    j = i - 1

    while j >=0 and numbers_list[j] > key:
        numbers_list[j + 1] = numbers_list[j]
        j -=1
    numbers_list[j + 1] = key
return numbers_list


#Binary search is efficent at working lists that have already been sorted with a 0(logn)
#Binary searches are much faster than linear searches on large lists

# The sorted list after Insertion Sort
numbers = [-40, -3, -1, 1, 2, 4, 5, 7, 9, 16, 18, 27, 35, 100]

def binary_search(numbers_list, target):
  
    low = 0
    high = len(numbers_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Search for 9
target = 9
index = binary_search(numbers, target)

if index != -1:
    print(f"Number {target} found at index: {index}")
else:
    print(f"Number {target} not found in the list")

#Databasesd use binary searches to quickly find something in a sorted list or table
#Dictionaries use a binary search to look up words in a ditionary 