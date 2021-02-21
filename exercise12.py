# write a python program to find whether a given number from user is even or odd
# print out an appropriate message to the user

number = int(input("Enter number "))

if number % 2 == 0:
    print(f" {number} is even")
else:
    print(f"{number} is odd")
