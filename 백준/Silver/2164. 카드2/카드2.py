from collections import deque
n=int(input())
array=deque([i for i in range(1,n+1)])
while len(array)!=1:
    array.popleft()
    array.rotate(-1)
print(array[0])