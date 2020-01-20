import random

minPrime=2
maxPrime=200

""" Checks if number is prime """
def isPrime(x):
    if(x==2):
        return True
    if(x%2==0):
        return False
    for i in range(3,x,2):
       if (x % i) == 0:
           return False
    return True

""" Returns the set of numbers that are not allowed to be keys """
def coPrimesSet(n,fn):
    coSet=set([])
    if(isPrime(n)):
        coSet.add(n)
    else:
        for i in range(2,n+1):
            if(n%i==0):
                coSet.add(i)
    if(isPrime(fn)):
        coSet.add(fn)
    else:
        for i in range(2,fn+1):
            if(fn%i==0):
                coSet.add(i)
    return coSet

""" Genereting keys """
print("Genereting keys...")
prime = [i for i in range(minPrime,maxPrime+1) if isPrime(i)]
p=0
q=0
while(p==q):
    p=random.choice(prime)
    q=random.choice(prime)
    if(p>q):
        q,p=p,q
n =p*q
fn= (p-1)*(q-1)
print("(p,q)=(",p,",",q,")")
print("n=",n)
print("fn=",fn)
""" Encription Key """
e=0
coSet=coPrimesSet(n,fn)
""" print("coSet",coSet) """
for i in range(2,fn):
    for j in coSet:
        if(i%j!=0):
            e=i
            break
print("Encription Key (e,n) is (",e,",",n,")")
"Decription Key"
d=e+1
while(True):
    if((d*e)%fn==1):
        break
    else:
        d+=1
print("Decription Key (d,n) is (",d,",",n,")")

""" Random message for encription"""
message=random.randrange(n+1)
print("message for encription is: ",message)

""" Encription """
cypher=(message**e)%n
print("cypher is: ",cypher)

"""Decription"""
solution=(cypher**d)%n
print("original message is: ",solution)