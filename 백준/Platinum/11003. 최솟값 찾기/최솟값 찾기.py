# 문제 10 / 최솟값 찾기 1
# https://www.acmicpc.net/problem/11003

from sys import stdin,stdout
from collections import deque

input=stdin.readline
print=stdout.write

N,L=map(int,input().split())
A=list(map(int,input().split()))
q=deque([(0,A[0])])
print(str(q[0][1])+' ')
for i in range(1,N):
  while q and q[-1][1]>=A[i]:
    q.pop()
  q.append((i,A[i]))
  if q[0][0]<i-(L-1):
    q.popleft()
  print(str(q[0][1])+' ')