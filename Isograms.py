def isIsogram(str1):
    str2 = ''
    str1 = str1.lower()
    for i in range(len(str1)):
        if str1[i] in str2:
            return False
        str2 += str1[i]
    return True

test = (input(""))
while test != '3':
    print(isIsogram(test))
    test = (input(""))
