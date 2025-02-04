""" Day 6 - Dictionaries
- Creating dictionaries, adding/removing items
- Accessing keys, values, and items
- Advanced dictionary methods: `.get()`, `.setdefault()`, `.update() """

#Arrays in Python
#list
#tuple
#set
#dictionary

#Dictionaries
#A dictionary is a collection of items that are unordered, changeable, and indexed.
#Dictionaries are an unordered collection of Key-Value pairs.
#Dictoinaries are written with curly brackets "{}".

#Creating a dictionary
new_dict = {'name': 'Paul', 'age': 3, 'height': 6}
another_dict = dict(name='Michael', age=10, height=5)

#Accessing value items in a dictionary
#Accessing using key assigned to that value
#print(another_dict['name'])

#Accessing using the .get() method
#print(another_dict.get('age'))

#Accessing keys in a dictionary
#The .keys() method is used to return a list of all keys in a dictionary
#print(another_dict.keys())

#Adding items to a dictionary
new_dict['email'] = 'abcd@gmail.com'


#Removing items from a dictionary
#The .pop() method is used to remove an item from a dictionary
#new_dict.pop('height')

#The .popitem() method is used to remove the last item from a dictionary
#print(new_dict.popitem())

#del keyword is used to remove an item from a dictionary
del new_dict['age']
#print(new_dict)


#Advanced dictionary methods
#The .setdefault method is used to get the value of a key if it exists or set a default value for the key if it doesn't exist
students_grades = {
    "John": 85,
    "Paul": 50,
    "Derek": 70
}
students_grades.setdefault('Alice', 65)

students_grades.setdefault('John', 100)


#The .update method is used to update the dictionary with key-value pairs to update the dictionary
newer_dict = {'John': 100}
students_grades.update(newer_dict)
print(students_grades)