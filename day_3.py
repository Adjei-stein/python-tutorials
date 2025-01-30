""" Day 3 - Strings and String Manipulation
- String creation and concatenation
- String slicing, indexing, and escaping special characters
- Common string methods (`.split()`, `.join()`, `.strip()`, `.replace()`, etc.) """

#Strings
#Strings are sequences of characters enclosed in single or double quotes
#- String creation and concatenation
#Single quotes - ''
#Double quotes - ""

'My name is Paul' #- That's known single line string
'''My name is Paul''' #- That's known as multi-line string

"""My name 

is Paul"""

text = "My name is "
text_2 = 'Paul'

print(text + text_2) #Output: My name is Paul



#- String slicing, indexing, and escaping special characters

#String slicing
#String slicing is the process of extracting a part of a string

#Slicing with starting and ending points
string = "Hello, World!"
print(string[7:12]) #Output: World

#Slicing in multiples
print(string[::2]) #Output: Hlo ol!

#String indexing
#String indexing is the process of accessing a character in a string
new_string = "Alphabet"
print(new_string[0]) #Output: A
print(new_string[-1]) #Output: t

#Escaping special characters
#Special characters are characters that have a special meaning in Python

#Escape character - '\'
#'My name is 'Paul'' #Output: SyntaxError: invalid syntax
print('My name is \'Paul\'') #Output: My name is 'Paul'
print("My name is 'Paul'") #Output: My name is 'Paul'
print("Hello, \"World\"!") #Output: Hello, "World"!


#Newline character - '\n'
print("""My name 
#is Paul""")
print("My age \nis 10")

#Tab character - '\t'
""" print("My name \tis Paul")
print("My name         is Paul") """

#Single quote - '\'' and double quote - '\"'
print("My name is \"Paul\"")


#- Common string methods (`.split()`, `.join()`, `.strip()`, `.replace()`, etc.)
#.split()
#The `.split()` method is used to split a string into a list of substrings based on a delimiter
string = "My name is Paul"
print(string.split('a'))

#.join()
#The `.join()` method is used to join a list of strings into a single string
texter = ['My', 'name', 'is', 'Paul']
print(''.join(texter))

#.strip()
#The `.strip()` method is used to remove leading and trailing whitespaces from a string
string = "    Hello, World!    "
print(string.strip())

#left strip
print(string.lstrip())

#right strip
print(string.rstrip())

#.replace()
#The `.replace()` method is used to replace a specified value in a string with another value
new = 'My name is Paul'
print(new.replace('Paul', 'Lawrence'))

#.lower()
#The `.lower()` method is used to convert a string to lowercase
new_upper = "THE QUICK BROWN FOX"
print(new_upper.lower())

#.upper()
#The `.upper()` method is used to convert a string to uppercase
new_lower = "the quick brown fox"
print(new_lower.upper())