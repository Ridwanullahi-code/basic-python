""" write a python code to calculate Range, maximum height and time of flight
"""

print("Welcome to physics python code")
print("calculation on motion ")
print("final velocity(m/s) initial velocity(m/s) time(s) distance(m) acceleration(m/s**2)")
print("v | u | t | d | a")
calc = input("Enter the value")
u = int(input("Enter The given initial velocity "))
v = int(input('Enter the given final velocity '))
a = int(input("Enter The given acceleration "))
t = int(input("Enter The given time "))
d = int(input("Enter The given distance "))

if calc == "a":
 	answer = (v-u)/t 
 	print(answer)
	
elif calc == "v":
	answer = u**2 + 2*(a)*(d) 
	print(answer)

elif calc == "t":
	answer = (v-u)/a
	print(answer)

elif calc == "d":
	answer = u*t + 0.5*(a)*(t**2)
	print(answer)