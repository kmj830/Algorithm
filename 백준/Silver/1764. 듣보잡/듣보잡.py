import sys
n,m=map(int,input().split())
a=set()
b=set()
for _ in range(n):
    a.add(sys.stdin.readline().strip())
for _ in range(m):
    b.add(sys.stdin.readline().strip())
c=a.intersection(b)
print(len(c))
for i in sorted(c):
    print(i)