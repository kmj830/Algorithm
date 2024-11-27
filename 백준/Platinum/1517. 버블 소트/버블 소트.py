# 문제 21 / 버블 정렬 프로그램2
# https://www.acmicpc.net/problem/1517

from sys import stdin
input=stdin.readline

def merge_sort(s,e):
  global sc
  if e-s<1: return
  m=int(s+(e-s)/2)
  merge_sort(s,m)
  merge_sort(m+1,e)
  for i in range(s,e+1):
    tmp[i]=a[i]
  k=s
  idx1=s
  idx2=m+1
  while idx1<=m and idx2<=e:
    if tmp[idx1]<=tmp[idx2]:
      a[k]=tmp[idx1]
      if idx1>k:
        sc+=(idx1-k)
      k+=1
      idx1+=1
    else:
      a[k]=tmp[idx2]
      if idx2>k:
        sc+=(idx2-k)
      k+=1
      idx2+=1
  while idx1<=m:
    a[k]=tmp[idx1]
    if idx1>k:
      sc+=(idx1-k)
    k+=1
    idx1+=1
  while idx2<=m:
    a[k]=tmp[idx2]
    if idx2>k:
      sc+=(idx2-k)
    k+=1
    idx2+=1
n=int(input())
a=list(map(int,input().split()))
tmp=[0]*(n)
sc=0
merge_sort(0,n-1)
print(sc)