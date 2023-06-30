n=int(input())
import sys
array=[int(sys.stdin.readline().rstrip()) for _ in range(n)]
array.sort()
[print(array[i]) for i in range(n)]