import math
print("What would you like to do?\n1.\tCalculate University fees \n2.\tCalculate Cost of a loan \n3.\tQuit the program ")
choice = int(input("\nYour choice:"))
while choice > 3 or choice < 1:
    choice = int(input("Your choice:"))
    
if choice == 1:
    amount = float(input("Enter the amount: R"))
    perc = float(input("Enter the increase (% p.a.): "))
    year = int(input("How many years: "))
    perc /= 100
    
    for i in range(year):
        amount += (amount * perc)
    
    print("R",round(amount,2),"payable in", year, "years")
elif choice == 2:
    princi = float(input("Enter the amount: R"))
    peri = float(input("How many months: "))
    inter = float(input("Enter the increase (% p.a.): "))
    inter/=100
    payment = (inter/(1 - (1 + inter)**(-peri)))*princi
    total = payment * 12 * peri
    cost = peri * payment - princi
    #cost= cost * 100//1/100
    
    print("This loan will cost you R",round(cost,2))    
elif choice == 3:
    print("Program has ended!!!")