def merge(items, sections, temporary_storage):
    (start1, end1), (start2, end2) = sections
    i, j, k = start1, start2, start1

    while i < end1 and j < end2:
        # CHANGED: compare by string length (descending)
        if len(items[i]) >= len(items[j]):
            temporary_storage[k] = items[i]
            i += 1
        else:
            temporary_storage[k] = items[j]
            j += 1
        k += 1

    while i < end1:
        temporary_storage[k] = items[i]
        i += 1
        k += 1

    while j < end2:
        temporary_storage[k] = items[j]
        j += 1
        k += 1

    for index in range(start1, end2):
        items[index] = temporary_storage[index]







def merge_sort(items):
# Get the length of the input list
    items_length = len(items)
# Create temporary storage for merging
    temporary_storage = [None] * items_length
# Initialise the size of subsections to 1
    size_of_subsections = 1
# Iterate until the size of subsections is less than the length of the


    while size_of_subsections < items_length:
# Iterate over the list in steps of size_of_subsections * 2
        for i in range(0, items_length, size_of_subsections * 2):
            first_section_start = i 
            first_section_end = min(i + size_of_subsections, items_length)
# Determine the start and end indices of the two subsections
# to merge.
            second_section_start = first_section_end

            second_section_end = min(
                first_section_end + size_of_subsections, items_length
            )

# Define the sections to merge
            sections = (
                (first_section_start, first_section_end), 
                (second_section_start, second_section_end,),
            )
# Call the merge function to merge the subsections
            merge(items, sections, temporary_storage)
# Double the size of subsections for the next iteration
        size_of_subsections *= 2
# Return the sorted list
    return items

items = [
    "barnes", "birmingham", "bath", "southampton", "portsmouth"
    ]
print("Before sorting:" , items)
merge_sort(items)
print("After sorting the items in the list:", items)