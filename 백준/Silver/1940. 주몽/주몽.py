import sys
n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
materials=sorted(list(map(int,sys.stdin.readline().split())))
i=0;j=n-1;count=0
while i<j:
    if materials[i]+materials[j]==m:
        count+=1
        i+=1;j-=1
    elif materials[i]+materials[j]<m:
        i+=1
    else:
        j-=1
print(count)