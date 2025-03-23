from data_structures.linked_list.linked_list import LinkedList
from algorithms.sorting.quick_sort import quick_sort

# Create a LinkedList instance
ll = LinkedList()

# Append values to the linked list
data_to_append = [3, 1, 4, 1, 5, 9, 2, 6]
for item in data_to_append:
    ll.append(item)

# Convert the linked list to a list
list_representation = ll.to_list()

# Sort the list using quick_sort
sorted_list = quick_sort(list_representation)

# Print the sorted list
print(sorted_list)
