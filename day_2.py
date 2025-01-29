""" Day 2 - Basic Operators
- Arithmetic, comparison, and logical operators (`+`, `-`, `*`, `/`, `and`, `or`, `not`)
- Using operators in practical scenarios """

#Arithmmetic Operators
#Operators used to perform basic mathematical operations
#Examples: +, -, *, /, %, **, //
#Additions: '+' operator
#Subtraction: '-' operator
#Multiplication: '*' operator
#Division: '/' operator
#Modulus: '%' operator
#Exponentiation: '**' operator
#Floor Division: '//' operator

#Addition
#Addition is the process of adding two or more numbers together
print(3 + 5) #Output: 8

#Subtraction
#Subtraction is the process of taking one number away from another
print(10 - 3) #Output: 7

#Multiplication
#Multiplication is the process of adding a number to itself a certain number of times
print(3 * 5) #Output: 15

#Division
#Division is the process of splitting a number into equal parts
print(10 / 2) #Output: 5.0

#Modulus
#Modulus is the process of finding the remainder of a division operation
print(10 % 3) #Output: 1

#Exponentiation
#Exponentiation is the process of raising a number to a power
print(2 ** 3) #Output: 8


#Floor Division
#Floor division is the process of dividing two numbers and rounding down to the nearest whole number
print(10 // 3) #Output: 3



#Comparison Operators
#Operators used to compare two values
#Examples: ==, !=, >, <, >=, <=
#Equal: '==' operator
""" NB: Assign: '=' operator
3 = 5 #Output: SyntaxError: can't assign to literal
var = 5 #Output: 5
print(var + 3) #Output: 8 """
a = 5
b = '5'
c = 5
d = 10
print(a == b) #Output: False
print(a == c) #Output: True
print(a == d) #Output: False

#Not Equal To
#Not equal to is the process of determining if two values are not equal
""" NB: '!=' operator is the opposite of the '==' operator """
print(a != b) #Output: True

#Greater Than
#Greater than is the process of determining if one value is greater than another
print(a > d) #Output: False

#Less Than
#Less than is the process of determining if one value is less than another
print(a < d) #Output: True

#Greater Than or Equal To
#Greater than or equal to is the process of determining if one value is greater than or equal to another
print(a >= c) #Output: True

#Less Than or Equal To
#Less than or equal to is the process of determining if one value is less than or equal to another
print(a <= d) #Output: True
print(a <= b) #Output: TypeError: '<=' not supported between instances of 'int' and 'str'




#Logical Operators
#Operators used to combine two or more conditions
#Examples: and, or, not
#And: 'and' operator
#The 'and' operator returns True if both conditions are True
age = 20
is_employee = True
print(age > 18 and is_employee) #Output: True

#Or: 'or' operator
#The 'or' operator returns True if one of the conditions is True
print(age > 18 or not is_employee) #Output: True

#Not: 'not' operator
#The 'not' operator returns True if the condition is False
print(age > 18 and not is_employee) #Output: False