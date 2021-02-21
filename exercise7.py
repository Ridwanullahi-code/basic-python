# write a python program to get difference between a given number and 17
# if the number is greater than 17 return double the absolute different

number = int(input("Enter the number"))
num_diff = number - 17
if num_diff > 17:
    print(num_diff **2)
