#Easy 
''' 
Question1 : You go to a shop Price of 1 item ="50" (string)
You buy 2 items. Calculate the total cost. 
Hint: Output should be a number, not a string.'''

 x = "50" #Price of 1 item string
 y = int(x) #change str to int
 total_price = 2*y #since 2 items were bought.
 print (total_price)

'''
Question 2: user input gives age as "21" (string). Print their age next year.'''

x ="21"
print(int(x)+1)

#Medium 
'''
Question 3: Temperature is given as "36.6" (string)

Convert it to float and print:

"Normal temperature" if ≥ 36.5
"Low temperature" if < 36.5 '''
x="36.6" #string 
temperature = float(x) #converts str to float
 if temperature>=36.5:
    print("Normal temperature")
 else :
    print("low temperature")


 '''
 3 friends go to a café:

Total bill = "450" (string)

Split equally and print how much each person pays.

Hint:Output should be a float.'''

total_bill = "450" 
total_bill = float(total_bill) #convert str to float
per_person_payment= total_bill/3
print(per_person_payment) 

#Hard
''' 
Question5: A person has:

Salary = "25000"
Bonus = 10% of salary

Calculate total salary after bonus.

Hint: Final answer should be numeric.'''

salary ="25000" # in str
salary =float(salary) #change to float 
bonus = (10/100)*salary #gives the bonus

total_salary= salary+bonus
print(int(total_salary))

'''
Question 6 :A student has marks:

"85"
"90.5"
"78"

These are strings, not numbers.

Task
Convert them into numbers
Calculate the average
Print the result'''


x="85"
y="90.5"
z="78"
x=float(x)
y=float(y)
z=float(z)
total = x+y+z
avg = total/3
print (avg)