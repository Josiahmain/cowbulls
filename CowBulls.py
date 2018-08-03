##game cowbulls
import random
cows=0 #scores for a number match out of position
bulls=0 #scores for a number match in position


def checknum(n):#checks for matches in list
  global cows
  if n in x:
    cows += 1
    x.remove(n)
  return
def checkmatch(n,N):#compares two values in same position of lists then deletes them for subsequent checks
  global bulls
  if n==N:
    bulls += 1
    x.remove(n)
    X.remove(N)
  return

print("Can you guess what 4 digit number I'm thinking of?")
print("If you guess a number correctly but out of place, you get a cow. If you guess a number ocrrectly in the correct position you get a bull. FYI once a number has been matched it cannot be matched again i.e 1112 and 0031 only scores 1 cow.")
print("Guess a 4 digit number")

a=random.randint(1,10)#creates random 4 digits
b=random.randint(1,10)
c=random.randint(1,10)
d=random.randint(1,10)
g=0 
while bulls<4:
  cows=0
  bulls=0
  x=[a,b,c,d]
  y=input()
  if len(y)!=4:
    print("please enter a 4 digit number")
    continue
  g+=1
  A=int(y[0])#could be written into loop
  B=int(y[1])
  C=int(y[2])
  D=int(y[3])
  X=[A,B,C,D]
  checkmatch(a,A)
  checkmatch(b,B)
  checkmatch(c,C)
  checkmatch(d,D)
  if bulls == 4:
    break
  for nums in X:
    checknum(nums)
  print(str(y)+" gives "+str(bulls)+" bulls and "+str(cows)+" cows")
  print("guess again")
print ("you have guessed the number in " +str(g)+" tries")

  
    
	
