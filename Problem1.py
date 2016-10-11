num_entered = []
num = int(input("Enter a number (-1 to stop): "))
num_entered.append(num)
while num != -1:
    num = int(input("Enter a number (-1 to stop): "))
    num_entered.append(num)
n = 0
m = 1
while num_entered[m] != -1:
    print(num_entered[n]+num_entered[m], end=' ')
    n += 1
    m += 1
    