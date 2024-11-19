# 문제 7 / 주몽의 명령
# https://www.acmicpc.net/problem/1940

N=int(input())
M=int(input())
material=sorted(list(map(int,input().split())))
s,e=0,N-1
answer=0
while s<e:
  result=material[s]+material[e]
  if result==M:
    s+=1
    answer+=1
  elif result<M:
    s+=1
  else:
    e-=1
print(answer)