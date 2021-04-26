# assign input function to variable name1 to make name1 to prompt enter name
name1 = input("Name1: ")

# assign input function to variable name2 to make name1 to prompt enter name
name2 = input("Name2: ")

# assign bonds to variable bond
bond = "bonds"

# this program join name1, bond, and name2 together using additional operator
join = name1 + bond + name2

# this program count the frequence of each letter occur and assign it to variable count
count = (join.count("R"),
	join.count("o"),
	join.count("s"),
	join.count("e"),
	join.count("b"),
	join.count("n"),
	join.count("d"),
	join.count("a"),
	join.count("c"),
	join.count("h"),
	join.count("l")
)

""" str() function cast count to str, join() string method join all
the converted count together and spit(",") remove the comma
 in the count variable elements
"""
# print count elements
# count = 22311111111
print("".join(str(count).split(",")))

"""this program assign element of count, using index number to get
 element of each element in count and added first element from left and
""" 
new_number1 = count[0] + count[10], count[1] + count[9], count[2] + count[8], count[3] + count[7], count[4] + count[6], count[5]
"""this program assign element of count, using index number to get
 element of each element in count and added first element from left and
""" 
new_number2 = new_number1[0] + new_number1[5], new_number1[1] + new_number1[4], new_number1[2] + new_number1[3]

""" str() function cast new_number1 to str, join() string method join all
the converted new_number1 elements together and spit(",") method remove the comma
 in the count variable elements
"""
b = "".join(str(new_number1).split(","))
# print new_number1 elements
# new_number1 = 334221
print(b)

""" str() function cast new_number2 to str, join() string method join all
the converted new_number2 elements together and spit(",") method remove the comma
 in the count variable elements 
"""
c = "".join(str(new_number2).split(","))
# print new_number2 element
# new_number2 = 456
print(c)

# new_number2 = 456
# added the first and last element in new_number2 together assign to variable step1 
#new_number2[0] + new_number2[2] = 4 + 6
#new_number2 = 10
step1 = new_number2[0] +  new_number2[2]

# assign middle element of new_number2 and assign to variable step2
# new_number2[1] = 5
step2 = new_number2[1]

# cast  step1 elements to string
# step3 = 10
step3 = str(step1)

# cast step2 variable to string
# step2  = 5
step4 = str(step2)

# print added step 3 and step 4 together, elements 10 + 5 = 105
# note the output will be 105 because it has casted to string not number
step5 = int(step3 + step4)
print(step5)

#cast first element of step3 variable to number
# step3[1] = 1  
step6 = int(step3[0])

#cast  last element of new_number2 variable to number
# recall step3 = 10
#step3[1] = 0
step7 = int(step3[1])

#cast   element of step4 variable to number
# step8 = 5
step8 = int(step4)

# added step8 and step8 together assign to variable step9
# step9 = 6
step9 = step8 + step6

# added  step9  and step7  to give 60
# step10 = 60
step10 = str(step9) + str(step7)

# print 60
print(step10)


