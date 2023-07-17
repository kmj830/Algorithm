import sys
input=sys.stdin.readline
n=int(input())
line=list(map(int,input().split()))
line.sort()
total=0
for i in range(1,len(line)+1):
    total+=sum(line[0:i])
print(total)