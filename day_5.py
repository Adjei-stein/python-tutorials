""" **Day 5 - Tuples and Sets**
- Immutable tuples: creation, unpacking, and indexing
- Understanding sets and set operations (union, intersection, difference)
- Using set methods (`.add()`, `.discard()`, `.pop()`) """

#Tuples
#A tuple is a collection of items that are ordered and unchangeable. 
#Tuples are written with round brackets.
#Tuples are immutable sequences of elements. They are similar to lists but cannot be changed after creation.
#Tuples are represented by parentheses "()".

#Creating a tuple
my_list = (1, 2 ,3)
my_list[2] = 10
print(my_list)

#Creating a tuple with mixed items
my_tuple = (1, 'Paul', 2.5, True)
print(my_tuple)

#Accessing items in a tuple
#indexing a tuple
print(my_tuple[1])
my_age = my_tuple[0]
my_name = my_tuple[1]

#Unpacking a tuple
my_age, my_name, my_height, is_student = my_tuple
print(my_age)
print(is_student)

#Understanding sets and set operations (union, intersection, difference)
#Sets
#A set is a collection of items that are unordered and unindexed.
#Sets are written with curly brackets "{}" or using the set function "set()"".
#Creating a set using curly brackets
my_set = {1, 2, 3, 4, 5}
print(my_set[2])

#Creating a set using set()
new_set = set([1, 2, 2, 3, 4, 5])
print(new_set)

#Set operations
#Changing positons in a set is impossible
new_set[1] = 10 #TypeError: 'tuple' object does not support item assignment
print(new_set)

#Adding an item to a set
#"Add()" method is used to add an item to a set
new_set = {1, 2, 3, 4, 5}
new_set.add(6)
print(new_set)

#Removing an item from a set
#"Discard()" method is used to remove an item from a set
new_set = {1, 2, 'Paul', 4, 5}
new_set.discard('Paul')
print(new_set)

#Union of sets
#The union of two sets is a set that contains all the items from both sets.
#Union of sets can be done using the "|" operator or the "union()" method.
first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8}
union_set = first_set | second_set
#union_set = first_set.union(second_set)
print(union_set)

#Intersection of sets
#The intersection of two sets is a set that contains all the items that are present in both sets.
#Intersection of sets can be done using the "&" operator or the "intersection()" method.
first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8}
intersection_set = first_set & second_set
#intersection_set = first_set.intersection(second_set)
print(intersection_set)

#Difference of sets
#The difference of two sets is a set that contains the items that are 
#present in the first set but not in the second set.
first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8}
print(second_set - first_set)