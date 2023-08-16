import sys
import heapq
input=sys.stdin.readline
N=int(input())
array=[];count=0
for i in range(N):
    heapq.heappush(array,int(input()))
for i in range(N-1):
    num=heapq.heappop(array)+heapq.heappop(array)
    count+=num
    heapq.heappush(array,num)
print(count)