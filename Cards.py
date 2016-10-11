import random
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
def shuffleDeck(d):
    for i in range(len(d)):
        f = random.randint(0,51)
        (d[f],d[i]) = (d[i],d[f])
    return d

def createDeck():
    return (list(range(52)))

def getSuit(i):
    return (suits[i%4])

def getRank(i):
    return ranks[int(i/4)]

def displayDeck(d,n):
    for i in range(n):
        print("Card number {0:2}: {1} of {2}".format(d[i],getRank(d[i]),getSuit(d[i])))
dec = createDeck()
shuffleDeck(dec)
displayDeck(dec,4)