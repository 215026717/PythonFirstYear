size = int(input("Size :"))
m=1
for row in range (size):
    s = " "
    for space in range(size - row - 1):
        s += " "
    for col in range(2 * row + 1):
       
        s += "#"
        m+=1
    print(s)