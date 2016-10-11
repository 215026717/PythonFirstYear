def isPalindrome():
    n = input()
    for i in range(int(len(n)/2)):
        if n[i].lower() != (n[(i+1)*-1]).lower():
            return("Not a Palindrome")
    return True        
print(isPalindrome())