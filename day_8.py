""" Day 8 - Loops and Iteration
- For loops, while loops, and loop control (`break`, `continue`, `else`, `pass`)
- Iterating over lists, tuples, dictionaries, and sets
- Pythons internal functions
- Looping with `range()` and custom iterable objects """

#Loops and Iteration
#Loops are used to execute a block of code multiple times
#Types of loops in Python
#1) For loop
#This is used to iterate over a sequence and perform actions on each element in that sequence


#Example;
#Looping through a list
my_list = [1, 2, 2, 3, 4, 5]
for number in my_list:
    print(number)


#Looping through a string
my_string = "Hello Paul!!!"
for text in my_string:
    print(text)

#2) While loops
#This repeatedly executes a block of code as long as a specific condition remains true

#Example;
counter = 0
while counter < 5:
    print(counter)
    counter +=1
""" NB: The plus symbol should be in front of the equal sign and not 
after if you want to assign a calculation of the previous 
counter plus a specific number to a new counter """

#loop control
#This is a statemment that modify the flow of execution inside loops
#Most common loop controls
#break
#continue
#else
#pass

#Example of loops without ends
counter = 0
while counter >= 0:
    print(counter)
    counter +=1

#1) Break
#This is a statement used to exit the loop permanently and prematurely when a specific condition is met
counter = 0
while counter >= 0:
    if counter >=5:
        break
    print(counter)
    counter +=1

#Continue
#This is a statement that skips the current iteration of the loop and moves onto the next one
counter = 0
while counter < 10:
    if counter == 5:
        counter +=1
        continue
    print(counter)
    counter +=1


#Else  
#It executes after the loop finishes all it's iterations without encountering a break
my_string = "Hello Paul!!!"
for text in my_string:
    if text == ' ':
        break
    print(text)
else:
    print("Done with for loop")

#Pass
#This is a null operator and doesn't do anything
counter = 0
while counter < 10:
    if counter == 5:
        pass
    else:
        print(counter)
    counter +=1

#Pythons internal functions
#Len()
new_array = [1, 2, 3, 4]
print(len(new_array))

#input()
var = input('What\'s your name? :')
print("User's namme is...", var)


#Looping with `range()` and custom iterable objects
#range()
print(range(5))
#For loop for range
for number in range(5):
    print(number)

#Iterating over a list
my_list = ['monkey', 'frog', 'pig']
for animal in my_list:
    print(animal)

#Iterating over a Tuple
dimensions = (10, 20, 30)
for dimension in dimensions:
    print(dimension)