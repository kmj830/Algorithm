import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
def isPrime(num):
  for i in range(2,int(num**0.5+1)):
    if num%i==0:
      return False
  return True

def dfs(num):
  if len(str(num))==n:
    print(num)
  else:
    for i in range(1,10,2):
      if isPrime(num*10+i):
        dfs(num*10+i)

dfs(2);dfs(3);dfs(5);dfs(7)