def displayAllRoutes(d):
    for i in range(6):
        print("Route {0}: {1}".format(i+1,d[i+1]))
def findRoute(s):
    count = 0
    for i in range(6):
        if s in d[i+1]:
            count = 1
            print("Route {0}: {1}".format(i+1,d[i+1]))
    return count
def selectRoute():
    ''''''


d = {1:"Durban - Pietermaritzburg – basic adult fare R50.00",2:"Durban - Port Edward – basic adult fare R75.00",3:"Durban - Richard’s Bay – basic adult fare R85.00",4: "Port Edward - Richard’s Bay – basic adult fare R155.00",5:"Pietermaritzburg - Port Edward – basic adult fare R100.00 ",
6: "Pietermaritzburg - Richard’s Bay – basic adult fare R130.00"}