# Author: Mongezi Nene
# Student number: 215026717
# Description: this is a menu that can calculate university fees or cost of a loan if the user wishes to do so

def unifees(): #function to determine University fees
    print("\n---You chose to calculate university fees---") #prints the users choice
    amount = float(input("\nEnter the amount: R"))
    while amount < 0: #while loop that ensures the amount is positive
        amount = float(input("Enter the amount {POSITIVE}: R"))
        
    perc = float(input("Enter the increase (% p.a.): ")) / 100
    while perc < 0 or perc > 1: #while loop that ensures the interest rate is within 0 and 100
        perc = float(input("Enter the increase ([0 - 100]% p.a.): ")) / 100
        
    year = int(input("How many years: "))
    while year < 0: #while loop that ensures the years value is positive
        year = int(input("How many years {POSISTIVE}: "))        
        
    print("") #prints empty string so lines will be neatly spaced
    for i in range(year): #for loop to calculate the cost for each year
        amount += (amount * (perc))
        print("Year", (i+1),"will cost you R %.2f" % amount) #prints the cost for each year (2 decimal places)
        
    if year == 1: #if statement for when value for years is singular
        print("\nR %.2f" % amount, "payable in", year, "year\n")
    else: #else statement executed when years value is plural
        print("\nR %.2f" % amount, "payable in", year, "years\n")

def loan_cost(): #function to determine the cost of loan
    print("\n---You chose to calculate cost of a loan---") #prints the users choice
    princi = float(input("\nEnter the amount: R"))
    while princi < 0: #while loop that ensures the principal is positive
            princi = float(input("Enter the amount {POSITIVE}: R"))  
            
    inter = float(input("Enter the increase (% p.a.): ")) / 100
    while inter < 0 or inter > 1: #while loop that ensures the interest rate is within 0 and 100
            inter = float(input("Enter the increase ([0 - 100]% p.a.): ")) / 100    
            
    peri = float(input("How many months: "))    
    while peri < 0: #while loop that ensures the period is positive
            peri = int(input("How many months {POSISTIVE}: "))        
            
    payment = (inter/(1 - (1 + inter)**(-peri)))*princi #payment on the loan per month
    cost = peri * payment - princi #total cost of the loan
    print("\nThis loan will cost you R %.2f" % cost, "\n") #prints how much the loan will cost (2 decimal places)
    
def menu(): #function that displays the menu
    print("What would you like to do?\n")
    print("1.  Calculate University fees")
    print("2.  Calculate Cost of a loan")
    print("3.  Quit the program")
    
choice = 1 #initial choice assigned to allow while condition to be true so to force the loop to be executed

while choice != 3:
    menu() #calling the menu function
    choice = int(input("\nYour choice: ")) #the user input for their choice on the menu
    
    while choice > 3 or choice < 1: #executed when the choice value is not valid for the given menu
        choice = int(input("Your choice [1-3]: ")) 
        
    if choice == 1:
        unifees() #calling the University fees function
    
    elif choice == 2:
        loan_cost() #calling the cost of loan function
    
print("\n---Program has ended!!!---") #print statement for when user chooses to end program