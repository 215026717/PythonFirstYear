n = 0
m = 0
wins = 0
loses = 0
draws = 0
n = int(input("Enter pairs of scores: \n"))
m = int(input())
if n > m:
        wins += 1
elif m > n:
        loses += 1
else:
        draws += 1
tot = 1
while (n != -1):
        n = int(input())
        if n == -1:
                break
        m = int(input())
        if n > m:
                wins += 1
        elif m > n:
                loses += 1
        else:
                draws += 1
        tot += 1
        
        
print("CS100 Record \nWins -", wins, "\nLoses -", loses, "\nDraws -", draws,"\nTotal games played: ", tot)
if loses == 0:
        print("Congratulations on your undefeated season")