import math
def PrimeFinder():
    sequence=[]
    prime=[]
    print("y = ax+b")
    k3=int(input('a : '))
    k4=int(input('b : '))
    print('================================================')
    k1=int(input('Starting value of x : '))
    k2=int(input('Ending value of x : '))
    for n in range(k1, k2+1):
        term=k3*n+k4
        sequence.append(term)
    for m in sequence:
        phi=0
        for i in range(m+1):
            if math.gcd(m,i)==1:
                phi=phi+1
            else:
                phi=phi+0
        if phi==m-1:
            prime.append(m)
    print(prime)
    print("The Number of Primes : ", len(prime))
    print()
    confirm=input("Want to find primes again?? (y/n)")
    if confirm=="y":
        PrimeFinder()
    else:
        exit()

PrimeFinder()
