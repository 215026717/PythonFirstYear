n = int(input("Enter a number :"))
m = 1
sums = 0
c = 1
other_sum = 0
d = 0
while (n % (10**(m-1))) != n:
    ad = n % (10 ** m)
    if ad > 9:
        ad = ad // (10 ** d)
    sums += ad
    m += 1
    d += 1
if sums >= 20:
    while sums % (10**(c-1)) != sums:
        ad = sums % (10 ** c)
        if ad > 9:
            ad //= (10 ** (c-1))
        other_sum += ad
        c += 1       
if other_sum == 3 or sums < 20 and sums % 3 == 0:
    print(n ,"is divisible by 3")
else:
    print(n,"is not divisible by 3")