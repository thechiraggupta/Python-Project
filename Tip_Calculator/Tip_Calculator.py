print("Welcome to the tip calculator!")
amount=int(input("What was the total bill?\n"))

percent=int(input("How much tip would you like to give? 10, 12 or 15?\n"))
amount2=amount*(percent/100)

new_amount=amount2+amount

person=int(input("How many people to split the bill?"))

total_amount=round(new_amount/person, 2)

print("Each person should pay:", total_amount)