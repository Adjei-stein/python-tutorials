#1) Create a code to check if a variable containing the number '9' is positive, negative or zero

""" coffivi_var=9
if coffivi_var<0:
    print ('Negative')
elif coffivi_var>0:
    print ('Positive')
else:
    print('Variable is Zero') """

number = 9
if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"
 
print(f"The number is {sign}.")
 
""" number = 9
if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"
print("The number is " + sign) """
 
 