from sys import stdin
from collections import deque
N,L=map(int,stdin.readline().split())
A=list(map(int,stdin.readline().split()))
array=deque([])
for i in range(N):
    while array and array[-1][0]>A[i]:
        array.pop()
    array.append((A[i],i))
    if i-array[0][1]>=L:
        array.popleft()
    print(array[0][0],end=" ")