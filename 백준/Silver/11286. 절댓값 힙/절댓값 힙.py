# 문제 14 / 절댓값 힙 구현하기
# https://www.acmicpc.net/problem/11286
from sys import stdin,stdout
input=stdin.readline
print=stdout.write
import heapq
a=[]
for _ in range(int(input())):
  ipt=int(input())
  if ipt==0:
    try:
      print(f"{heapq.heappop(a)[1]}\n")
    except:
      print('0\n')
  else:
    heapq.heappush(a,(abs(ipt),ipt))