# write a python to test whether a number is within 100 0f 1000 0r 2000
def near_thousand(n):
    return ((abs(1000-n) <= 100) or (abs(2000-n) <=100))
print(near_thousand(1000))
print(near_thousand(900))
print(near(800))
