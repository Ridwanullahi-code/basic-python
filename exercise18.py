import cmath
opp = int(input("Enter opposite values: "))
adj = int(input("Enter adjacent values: "))
def cal_hypo():
    global opp
    global adj
    return cmath.sqrt(opp**2 + adj**2)
print(cal_hypo())