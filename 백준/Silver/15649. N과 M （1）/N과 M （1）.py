n,m=map(int,input().split())
array=list(range(1,n+1))
import itertools
for i in itertools.permutations(array,m):
    for j in i:
        print(j,end=" ")
    print()