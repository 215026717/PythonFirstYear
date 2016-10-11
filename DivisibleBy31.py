n = 1
while n > 0:
    n = int(input("Enter integer (-ve number to stop):"))
    trunc = n
    if trunc > 372:
        while trunc > 372:
            m = trunc // 10
            last = (trunc % 10) * 3
            trunc = m - last
            if trunc < 372:
                break
        if trunc % 31 == 0:
            print("(Reduced number:", trunc,end=") Divisible by 31\n")
        else:
            print("(Reduced number:", trunc,end=") NOT Divisible by 31\n")
            
    elif n % 31 == 0 and n > 0:
        print("(Reduced number:", trunc,end=") Divisible by 31\n")
    elif n % 31 != 0 and n > 0:
        print("(Reduced number:", trunc,end=") NOT Divisible by 31\n")
        