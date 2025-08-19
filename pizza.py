size = input("Which size would you like to order small,medium or large, type S,M,L respectively ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

pepperoni = input("Would you like pepperoni")
if pepperoni == "Y":
    if size == "S":
        bill += 1
    else:
        bill += 2

cheese = input("Would you also like to add cheese")
if cheese == "Y":
    bill += 3

print(f"Your final bill is ${bill}.\nEnjoy the pizza!")
