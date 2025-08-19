height = int(input("Enter your height: "))
bill = 0
if height >= 60:
    print("Go for it!")
    age = int(input("Enter your age: "))
    
    if age < 12:
        bill = 5
        print("Bill is $5")
            
    elif age <= 18:
        bill = 7
        print("Bill is $7")

    elif age>=45 and age<=55:
        bill = 0
        print("No bill")
        
    else:
        bill = 10
        print("Bill is $10")

    wants_photo = input("Do you want a picture? Yes or No ")
    if wants_photo == "y":
        bill +=3

    print(f"Your final bill is ${bill}")


else:
    print("Grow your height first")
