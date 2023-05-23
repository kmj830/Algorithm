N,M=map(int,input().split())
basket=[i+1 for i in range(N)]
for i in range(M):
    i,j=map(int,input().split())
    basket[i-1:j]=list(reversed(basket[i-1:j]))
for i in basket:
    print(i,end=" ")