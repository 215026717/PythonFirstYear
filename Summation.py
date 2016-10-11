numer = 1
denom = 3
quot = numer / denom
while denom < 99:
    numer += 2
    denom += 2
    quot += (numer / denom)
print(quot)