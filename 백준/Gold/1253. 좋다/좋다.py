import sys
input=sys.stdin.readline

n=int(input())
a=sorted(list(map(int,input().split())))
count=0
for i in range(len(a)):
  num=a[i]
  s,e=0,n-1
  while s<e:
    temp=a[s]+a[e]
    if temp==num:
      if s!=i and e!=i:
        count+=1
        break
      elif s==i:
        s+=1
      elif e==i:
        e-=1
    elif temp<num:
      s+=1
    else:
      e-=1
print(count)