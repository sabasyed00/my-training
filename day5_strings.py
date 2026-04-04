'''
Strings - surrounded by either single or double quotation marks
'hello' is the same as "hello"
'''
#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Jhonny'")

#Assign string to a variable 
a ="hello"
print(a)

#Multiline string
z = """ Hello ! This is my digital coding notebook.
        I hope these notes will be helpful to all.
        I need to improve my coding skills everyday"""
print(z)

#or you could use ''' .......... '''

''' Strings are arrays
  strings in Python are arrays of unicode characters.
  However, Python does not have a character data type, a single character is simply a string with a length of 1.'''

#Square brackets can be used to access elements of the string.

#Get the character at position 1 
#First character has the position 0

a = "Hello"
print(a[1])

#Looping through a string 

for x in "banana":
    print(x)

#String length 
#The len() func returns the length of a string 
a = "Hello"
print(len(a))

#Check string  - to check if certain phrase or character is present in a string, we can use the keyword in 

#Check if "rush" is present in the string 

text = "Wise men say only fools rush in"
print("rush" in text)

#use with if statement 

text = "Wise men say only fools rush in"
if "rush" in text:
    print("Yes,'rush' is present.")


#Check if not - to check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

text = "Wise men say only fools rush in."
print("take" not in text)

#use it with if statement 
text = "Wise men say only fools rush in."
if "take" not in text:
 print("take" not in text)
