words = ""
for i in range(int(input(""))):
    words += (",%s"%input(""))
out = {}
for i in range(int(input(""))):
    out[i] = ""
    for d in (input("")).split():
        if d not in words:
            out[i] += (" "+d)
for i in out.keys():
    print("Case #%d:%s"%(i+1,out[i]))