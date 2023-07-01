import sys
n,m=map(int,input().split())
a=set()
b=set()
[a.add(i) for i in sys.stdin.readline().split()]
[b.add(i) for i in sys.stdin.readline().split()]
c=a.difference(b)
d=b.difference(a)
e=c.union(d)
print(len(e))