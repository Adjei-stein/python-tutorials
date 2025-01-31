""" Day 4 - Lists and List Comprehension
- Creating, accessing, and modifying lists
- List methods (`.append()`, `.extend()`, `.insert()`, `.remove()`, etc.) """

#Lists
#A list is a collection of items that are ordered and changeable. Lists are written with square brackets.

#Creating a list
#Creating an empty list
my_list = []
print(my_list)

#Creating a list with items
my_list = [1, 2, 3, 4, 5]
print(my_list)

#Creating a list with different items
my_list = [1, 'Paul', 2.5, True]
print(my_list)

#Accessing items in a list
my_list = [1, 2, 3, 4, 5]
print(my_list[1])

#Accessing a list of items in a list
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])

#Accessing items in a list using negative indexing
my_list = [1, 2, 3, 4, 5]
print(my_list[-1])

#Accessing a list of items in a list using negative indexing
my_list = [1, 2, 3, 4, 5]
print(my_list[-4:-1])
#starting_point:end_point:step

#Modifying items in a list
#Changing an item in a list
my_list = [1, 2, 3, 4, 5]
my_list[2] = 10
print(my_list)

#Changing a list of items in a list
my_list = [1, 2, 3, 4, 5]
my_list[1:4] = [10, 20, 30]
print(my_list)

#List methods
#The append() method is used to add an item to the end of a list
my_list = [1, 2, 3, 4, 5]
my_list.append('6')
print(my_list)

#The extend() method is used to add items from another list to the end of a list
my_list = [1, 2, 3, 4, 5]
my_second_list = [6, 7, 8]
my_third_list = [9, 10]
""" The example below shows how to add items from my_second_list and my_third_list to my_list.
However, the items in my_second_list and my_third_list remain unchanged. """
print(my_list + my_second_list + my_third_list) #Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list) #Output: [1, 2, 3, 4, 5]
my_second_list.extend(my_third_list)
my_list.extend(my_second_list)
""" The example below shows how to add items from my_second_list and my_third_list to my_list. 
The items in my_list, my_second_list and my_third_list are changed and saved perfectly. """
print(my_list)

#The insert() method is used to add an item at a specified index in a list
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 'Paul')
print(my_list) #Output: [1, 2, 'Paul', 3, 4, 5]

#The remove() method is used to remove an item from a list
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list) #Output: [1, 2, 4, 5]

#The pop() method is used to remove an item at a specified index in a list
"""NB: Pop() method removes the last item in a list if no index is specified"""
my_list = [1, 2, 3, 4, 5]
my_list.pop()
print(my_list) #Output: [1, 2, 3, 4]

my_new_list = [1, 2, 3, 4, 5]
my_new_list.pop(3)
print(my_new_list) #Output: [1, 2, 3, 5]
