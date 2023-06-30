n=int(input())
import sys
array=[sys.stdin.readline().strip() for _ in range(n)]
array=list(set(array))
array.sort(key=lambda x:(len(x),x))
print(*array,sep="\n")