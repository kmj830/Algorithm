import sys
input=sys.stdin.readline
A,B=map(int,input().split())
array=[False,False]+[True]*int(B**0.5-1)
primes=[2]
for i in range(3,int(B**0.5)+1,2):
    if array[i]:
        primes.append(i)
        for j in range(2*i,int(B**0.5)+1,i):
            array[j]=False
count=0
for num in primes:
    temp=num*num
    while temp<=B:
        if temp>=A:
            count+=1
        temp=temp*num
print(count)