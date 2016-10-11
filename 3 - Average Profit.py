def mean(M,o):
    mean = 0
    for i in range(M):
        mean += o[i]
    for i in range(M)


T = int(input())
for i in range(T):
    s = input()
    N = 0
    o = []
    for d in range(len(s)):
        if s[d] == ' ':
            break
        N = (N * 10) + int(s[d])
    M = int(s[d+1:len(s)])
    for d in range(N):
        P = int(input())
        o.append(P)