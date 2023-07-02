a=[False,False]+[True]*(123456*2)
primes=[]
for i in range(2,123456*2+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i,123456*2+1,i):
            a[j]=False
import sys
while True:
    n=int(sys.stdin.readline().strip())
    if n==0:
        break
    temp=[i for i in primes if i>n]
    temp=[i for i in temp if i<=2*n]
    print(len(temp))