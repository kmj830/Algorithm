import sys
input=sys.stdin.readline
n=int(input())
A=list(map(int,input().split()))
A.sort()
count=0
for num in range(n):
    find=A[num]
    i=0;j=n-1
    while i<j:
        if A[i]+A[j]==find:
            if i!=num and j!=num:
                count+=1
                break
            elif i==num:
                i+=1
            else:
                j-=1
        elif A[i]+A[j]>find:
            j-=1
        else:
            i+=1
print(count)