n=int(input())
import sys
array=[sys.stdin.readline().strip().split() for _ in range(n)]
array.sort(key=lambda x:int(x[0]))
[print(f"{array[i][0]} {array[i][1]}") for i in range(n)]