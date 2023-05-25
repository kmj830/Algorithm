board=[[0 for j in range(100)]for i in range(100)]
for _ in range(int(input())):
    L,B=map(int,input().split())
    for i in range(L,L+10):
        for j in range(B,B+10):
            board[i][j]=1
sum=0
for i in range(100):
    for j in range(100):
        if board[i][j]==1:
            sum+=1
print(sum)