import math
def NameSur():
    N_s = input("Enter your name followed by a space then your surname :")
    for i in range(len(N_s)):
        if N_s[i-1] == ' ':
            sur = N_s[i:(len(N_s))]
    sur += " "
    return (sur+N_s[0])
def NormalPay():
    hours = math.ceil(float(input("Enter the amount of normal hours worked :")))
    while hours > 40 or hours <  0:
        hours = math.ceil(float(input("Enter the amount of normal hours worked(UP TO 40 HOURS) :")))        
    pay = hours * 50
    return pay
def Overtime():
    over_h = int(input("Overtime hours worked :"))
    over_m = int(input("Overtime mins worked :"))
    over = float(over_h + (over_m /60))
    pay = over * (50 * 1.5)
    return pay
def TaxDed(pay, over):
    ded = (pay + over) * (15 / 100)
    return ded
def Final(pay, over):
    final = (pay + over) * (85 / 100)
    return final
Name = NameSur()
norm = NormalPay()
over = Overtime()
print("\n"+Name)
print("Normal salary before tax: R%.2f" %norm)
print("Overtime salary before tax: R%.2f" %over)
print("Tax deducion: R%.2f" %TaxDed(norm, over))
print("Final salary:R%.2f" %Final(norm, over))