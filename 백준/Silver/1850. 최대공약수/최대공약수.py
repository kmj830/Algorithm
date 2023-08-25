import sys
input=sys.stdin.readline
a,b=map(int,input().split())
if a>b:
    a,b=b,a
while b%a!=0:
    b,a=a,b%a
print(str(1)*a)