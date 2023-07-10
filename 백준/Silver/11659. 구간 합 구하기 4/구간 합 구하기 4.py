import sys
n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
s=[]
for i in range(n):
    try:
        s.append(s[i-1]+nums[i])
    except:
        s.append(nums[i])

for _ in range(m):
    i,j=map(int,sys.stdin.readline().split())
    if i-2<0:
        print(s[j-1])
    else:
        print(s[j-1]-s[i-2])