import sys
input=sys.stdin.readline
n=int(input())
array=[False,False]+[True]*(9999999)
for i in range(2,10000000):
    if array[i]:
        for j in range(i*2,10000000,i):
            array[j]=False
while True:
    temp=str(n)
    if array[n]:
        for i in range(len(temp)//2):
            if temp[i]!=temp[-i-1]:
                break
        else:
            print(n)
            break
    n+=1