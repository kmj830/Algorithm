import sys
input=sys.stdin.readline
N,K=map(int,input().split())
A=[];count=0
for _ in range(N):
    A.append(int(input()))
for i in range(N-1,-1,-1):
    if A[i]<=K:
        count+=K//A[i]
        K=K%A[i]
print(count)