import sys
sys.setrecursionlimit(10**7)

def erase(n,r,c):
    if n>=3 and temp[r][c]==1 and r<N:
        for i in range(r+(n//3),r+(n//3)*2):
            for j in range(c+(n//3),c+(n//3)*2):
                temp[i][j]=0
    if n+r<N or n+c<N:
        if n+c<N:
            c+=n
        else:
            c=0
            r+=n
        erase(n,r,c)
    else:
        if (n//3!=1):
            r=0
            c=0
            return erase(n//3,0,0)

        

def temp_print():
    for i in range(N):
        for j in range(N):
            if temp[i][j]==1:
                print('*',end="")
            else:
                print(' ',end="")
        print()
N=int(input())
temp=[[1 for _ in range(N)]for _ in range(N)]
erase(N,0,0)
temp_print()