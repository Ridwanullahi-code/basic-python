# write a python program to solve (x+y)*(x+y)
def data(x,y):
	return (x+y)*(x+y)
print(data(20,10))

""" write a python program to convert all unit of time into seconds
"""
print("Hour | Minute | Second ")

unit = input("Enter the unit ")

time = input("ENTER THE UNIT TO CONVERT TO ")

time_num = int(input("Enter the unit to unit number "))

if unit == "Hour" and time == "Minute":
	conversion = time_num * 60
	print(conversion)

elif unit == "Hour" and time == "Second":
	conversion = time_num * 360
	print(conversion)

if unit == "Minute" and time == "Second":
	conversion = time_num *60
	print(conversion)

elif unit == "Minute" and time == "Hour":
	conversion = time_num/60
	print(conversion)

if unit == "second" and time == "Hour":
	conversion = time_num/360
	print(conversion)

elif unit == "second" and time == "Minute":
	conversion = time_num/60
	print(conversion)

