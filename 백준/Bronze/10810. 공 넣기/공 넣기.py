N,M=map(int,input().split())
basket=[0 for i in range(N)]
for i in range(M):
    i,j,k=map(int,input().split())
    for num in range(j-i+1):
        basket[i+num-1]=k
for i in basket:
    print(i,end=" ")