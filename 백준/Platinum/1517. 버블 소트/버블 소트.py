import sys
input=sys.stdin.readline
result=0
def merge_sort(s,e):
  global result
  if e-s<1: return
  m=int(s+(e-s)/2)
  merge_sort(s,m)
  merge_sort(m+1,e)
  for i in range(s,e+1):
    tmp[i]=a[i]
  k=s
  index1=s
  index2=m+1
  while index1<=m and index2<=e:
    if tmp[index1]>tmp[index2]:
      result+=index2-k
      a[k]=tmp[index2]
      k+=1
      index2+=1
    else:
      a[k]=tmp[index1]
      k+=1
      index1+=1
  while index1<=m:
    a[k]=tmp[index1]
    k+=1
    index1+=1
  while index2<=e:
    a[k]=tmp[index2]
    k+=1
    index2+=1
  

n=int(input())
a=[0]+list(map(int,input().split()))
tmp=[0]*(n+1)
merge_sort(1,n)
print(result)