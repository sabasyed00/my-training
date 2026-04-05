#This question would use a loop 

#What is a loop?
# To do something again and again.

#To print numbers 1 to 5 instead of write the print statement 5 times.

#we use a loop to optimize the code.

for i in range (1,6):
    print(i)


#Two types of loops 
''' - for 
    - while 
'''

#1.To print 1 to 10 
for i in range(1,11):
 print(i)

#2.To print even numbers
for i in range(2, 11,2):
 print(i)

''' 
2 - start
11 - end
2 - step  - how much you jump each time .
'''
#3.loop through list

nums = [10,20,30]

for n in nums:
  print (n)

#While loop
#runs until the condition becomes false

i=1
while i<=5:
  print(i)
  i+=1

#Reverse counting 
for i in range(10,0,-1):
  print(i)
  #print table of 5
  for i in range(1,11):
    result= 5*i
    print(5,'x',i,'=',result)
    