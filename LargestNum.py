n = int(input("Enter number here :"))
m = n
highest = n
lowest = n

if n == 0:
    print()
else:
    while (n != 0):
        n = int(input("Enter number here :"))
        m += n
        if highest < n:
            highest = n
        if lowest > n and n != 0:
            lowest = n
        
    print("Total is", m, "highest is", highest, "lowest is", lowest)