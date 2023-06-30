n=int(input())
import sys
array=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
array.sort(key=lambda x:(x[0],x[1]))
[print(f"{array[i][0]} {array[i][1]}") for i in range(n)]