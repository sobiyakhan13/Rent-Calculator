print("welcome to rent calculator !!")

## inputs we need from the user
# total rent
# total food ordered for snacking
# electricity units spend
# charge per unit
# number of people living in room/apartment

## outputs
# total amount you have to pay is


rent = int(input("enter your room/apartment rent:"))
food = int(input("enter the amount of food ordered:"))
electricity_spent = int(input("enter the total of electricity spent:"))
charge_per_unit = int(input("enter the charge per unit electricity:"))
people = int(input("enter the number of people living in flat/apartment:"))

total_bill = electricity_spent*charge_per_unit

output = (food + rent + total_bill) // people

print("each person will pay:", output)
input("\npress enter to exit...")
