total_bill = float(input("Enter the total bill: "))
tip = int(input("How much do you want to tip '5%', '10%' or '12%'? "))
if tip == 5:
    total_bill = ((total_bill)*(5/100))+total_bill
elif tip ==10:
    total_bill = ((total_bill)*(10/100))+total_bill
elif tip == 12:
    total_bill = ((total_bill)*(12/100))+total_bill
else:
    print(total_bill)

people = int(input("How many people are splitting the bill? "))
bill_on_each = "{:.2f}".format(total_bill/people)

print(f"Each one should pay {bill_on_each}")
