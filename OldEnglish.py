n = input("Enter your phrase: ")
count = 0
for i in range(len(n)):
    if n[i] in "sS":
        count += 1
n = n.replace('s','f')
n = n.replace('S','F')

print('In Old English:',n)
print("Changed",count,"letters")