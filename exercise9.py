# write a python program to calculate the sum of three given numbers
# if the values are equal then return three times of their sum

def sum_of_numbers(a,b,c):
    sum_numbers = a+b+c

    if a == b == c:

        return (sum_numbers)**3
    
print(sum_of_numbers(2,3,4))
print(sum_of_numbers(3,3,3))
