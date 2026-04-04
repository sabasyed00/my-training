#There are three numeric types in Python
#int
#float
#complex

#Creating a numeric type
x = 1 #int
y = 2.7 # float
z = 1j  #complex

#To verify the type of object in Python use the type() function

print(type(x))

#Int : whole number,positve or negative, without decimals, of unlimited length
x= 1
y=34253547927298
z = -36453827

#float : floating point number nummber,positive or negative,containing one or more decimals
x= 1.10
y=1.0
z=-35.54

#float can also be scientific number with an "e" to indicate the power of 10
x= 35e3
y=12E4
z=-76.3e100

#Complex
x=4+5j
y=8j
z=-4j

#Type conversion 
#use int() , float() , complex()

x = 1
y = 2.1
z = 2j
#convert from int to float 
a = float(x)
#convert from float to int
b = int(y)
#convert from int to complex
c = complex(x)

print (a)
print (b)
print (c)

# Random number
#Python has a built-in module called random

import random 
print(random.randrange(1,10))
