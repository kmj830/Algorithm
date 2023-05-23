N,M=map(int,input().split())
basket=[0 for i in range(N)]
for i in range(M):
    i,j,k=map(int,input().split())
    a=[k for i in range(j-i+1)]
    basket[i-1:j]=[k for i in range(j-i+1)]
for i in basket:
    print(i,end=" ")