#Daily problems 
'''Problem: Food Bill Split

You went to a restaurant with your friends.
Write a Python program that:
Takes the total bill amount as input
Takes the number of people as input
Calculates how much each person should pay'''

total_bill = input("Enter your total bill amount:")
total_bill = (float(total_bill))
print(total_bill)

number_of_people = input("Enter the total number of people:")
number_of_people =(int(number_of_people))
print(number_of_people)

if (number_of_people == 0):
 print("total_payment =" ,total_bill)
else :
 per_person_payment = (total_bill / number_of_people)
 print(per_person_payment)
