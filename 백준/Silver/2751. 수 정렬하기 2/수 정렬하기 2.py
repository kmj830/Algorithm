import sys
input=sys.stdin.readline
n=[]
for _ in range(int(input())):
  n.append(int(input()))
for i in sorted(n):
  print(i)