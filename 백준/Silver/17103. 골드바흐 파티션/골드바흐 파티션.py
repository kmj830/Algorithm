import sys
input=sys.stdin.readline

def prime_number(n):
  array=[False]*2+[True]*(n-1)
  for i in range(2,n+1):
    if array[i]:
      j=2
      while i*j<n+1:
        array[i*j]=False
        j+=1
  return array

array=prime_number(1000000)

for _ in range(int(input())):
  num=int(input())
  cnt=0
  for i in range(num//2+1):
    if array[i] and array[num-i]:
      cnt+=1
  print(cnt)