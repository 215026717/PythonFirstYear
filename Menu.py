def unifees(): #function to determine University fees
    amount = float(input("\nEnter the amount: R"))
    perc = float(input("Enter the increase (% p.a.): ")) / 100
    year = int(input("How many years: "))    
    for i in range(year):
        amount += (amount * (perc))
    print("\nR",round(amount,2),"payable in", year, "years\n")

def loan_cost(): #function to determine the cost of loan
    princi = float(input("\nEnter the amount: R"))
    inter = float(input("Enter the increase (% p.a.): ")) / 100
    peri = float(input("How many months: "))    
    payment = (inter/(1 - (1 + inter)**(-peri)))*princi
    total = payment * 12 * peri
    cost = peri * payment - princi
    print("\nThis loan will cost you R",round(cost,2),"\n")
    
def menu(): #function that displays the menu
    print("What would you like to do?\n")
    print("1.  Calculate University fees")
    print("2.  Calculate Cost of a loan")
    print("3.  Quit the program")
    
choice = 1 #initial choice assigned to allow while condition to be true so to force the loop to be executed

while choice != 3:
    menu() #calling the menu function
    choice = int(input("\nYour choice:")) #the user input for their choice on the menu
    
    while choice > 3 or choice < 1: #executed when the choice value is not valid for the given menu
        choice = int(input("Your choice [1-3]:")) 
        
    if choice == 1:
        unifees() #calling the University fees function
    
    elif choice == 2:
        loan_cost() #calling the cost of loan function
    
print("Program has ended!!!") #print statement for when user chooses to end program
    