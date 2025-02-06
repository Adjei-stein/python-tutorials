"""
Day 7 - Conditionals (if, elif, else)
- Writing multiple conditions and using nested if-else
- `if`-`elif` chains and boolean expressions
- Ternary operators and short-circuit logic
"""

#Conditionals
#Conditionals allow us to execute certain codes based on 'True' or 'False' statements/judgements
""" if condition:
    data/operations """

#If-else nesting
""" name = 'kofi'
if name == 'Kwame':
    print('Name was Kwame')
else:
    print('Name was NOT Kwame') """


#if-else-elif --Invalid Nesting
#if-elif-else --Valid
#if-else --Valid

#If-elif-else nesting
""" name = 'kwame'
age = 10
school = 'De Youngster'

if name == 'Kwame' and age == 11:
    print('Original Kwame found')
elif name == 'Kwame' and school == 'Light Academy':
    print('Wrong Kwame found')
else:
    print('Expected Kwamme does not exist') """


#Using If-else with mathematical operations
first_num = 20 #True
second_num = 7
#third_num = null #FALSE
""" if second_num >= first_num:
    print('Second is as high or higher than first number')
else:
    print('First is as higher than Second number') """

""" if 7 * 20 == 30:
    print('7 times 20 is 30')
else:
    print('7 * 20 is not 30') """

#Boolean Expression

""" if first_num:
    print('First num is true')
else:
    print('First num is not True') """

#Ternary Operator
status = 'First num is true' if first_num else 'First num is not True'
#print(status)

#Short-circuit logic
#And - Requires both first and last conditions to be true
#or - Requires only/at least one condition to be true

if first_num and not second_num:
    print('Valid')
else:
    print('Invalid')