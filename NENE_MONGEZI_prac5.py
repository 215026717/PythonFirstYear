__author__ = 'mongezi'
def inverse_add_vectors(u, v):
    return list(map(lambda a,b: a+b,u,v[::-1]))

def scalar_mult_matrix(s, m):
    return list(map((lambda a,b:(list(map((lambda c,d:c*d),[s]*len(b),b)))),[s]*len(m),m))            

def distance_vectors(u,v):
    l = 0
    for i in range(len(u)):
        l += ((u[i] - v[i])**2)
    list(map((lambda a,b:(b-a)**2),u,v))
    return float(l**(0.5))


