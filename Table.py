#program for finding table of any number upto 10 alues

#x_table variable, for desired number
x_table = int(input("Enter desired number for table: "))

#a varible containing the number's multiple of 10
multiplied_by_10 = x_table*10

#setting a counter for 1 to 10
multiplier = 1

#storing the result
result = multiplier*x_table

#using a while loop
while result <=multiplied_by_10:
    print(result)
    multiplier += 1
    result = multiplier*x_table

print("Done")
