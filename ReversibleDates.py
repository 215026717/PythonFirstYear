def isReversible(x,y,year):
    unrev = int("%d%d%d" %(x,y,year%100))
    rev = int("%d%d%d" %(year%100,y,x))
    if unrev == rev:
        return True
    return False

def usDate(day, month, year, seperator):
    return "%d%s%d%s%d" %(month,seperator,day,seperator,year%100)

def saDate(day, month, year, seperator):
    return "%d%s%d%s%d" %(day,seperator,month,seperator,year%100)

print("Welcome to the Reversible Date Program:")

while 3==3:
    day = int(input("Enter day: "))
    if day == 0:
        print("Good bye")
        break
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    seperator = input("Enter separator (- or /): ")
    
    if isReversible(month,day,year):
        print("\nUS date (%s)reversible"%(usDate(day, month, year, seperator)))
    else:
        print("\nUS date (%s)not reversible"%(usDate(day, month, year, seperator)))
    if isReversible(day,month,year):
        print("SA date (%s)reversible\n"%saDate(day, month, year, seperator))
    else:
        print("SA date (%s)not reversible\n"%(saDate(day, month, year, seperator)))