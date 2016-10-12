n = open('num.txt','r')
s = n.read()
num = 0
count = 0
sum1 = 0
sum2 = 0
highest = 0
num1 = 0
for i in range(len(s)):
    if s[i] == '\n':
        num += sum1
        lowest = sum1
        sum1 = 0
        count += 1
        continue
    else:
        sum1 = (sum1 * 10) + int(s[i])
    if sum1 > highest:
        highest = sum1
ave = num/count
print("Total count:\t{0:<}".format(count))
print("Average:\t{0:<}".format(ave))
for i in range(len(s)):
    if s[i] == '\n':
        num1 += (sum2-ave)**2
        if lowest > sum2:
            lowest = sum2        
        sum2 = 0
        continue
    else:
        sum2 = (sum2 * 10) + int(s[i])

std = (num1 / count) ** (0.5)
print("Standard Deviation:\t{0:<}".format(std))
print("Maximum:\t{0:<}".format(highest))
print("Minimum:\t{0:<}".format(lowest))