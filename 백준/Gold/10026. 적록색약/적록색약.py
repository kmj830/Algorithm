import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)


def navi(y,x):
    test_board[y][x]=count
    now=board[y][x]
    if y!=n-1 and now==board[y+1][x] and test_board[y+1][x]==-1:
        test_board[y+1][x]=count
        navi(y+1,x)
    if y!=0 and now==board[y-1][x] and test_board[y-1][x]==-1:
        test_board[y-1][x]=count
        navi(y-1,x)
    if x!=n-1 and now==board[y][x+1] and test_board[y][x+1]==-1:
        test_board[y][x+1]=count
        navi(y,x+1)
    if x!=0 and now==board[y][x-1] and test_board[y][x-1]==-1:
        test_board[y][x-1]=count
        navi(y,x-1)

def tbprint():
    for i in range(n):
        for j in range(n):
            print(test_board[i][j],end=' ')
        print()
    print()

def bprint():
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=' ')
        print()
    print()


def getmax():
    grt=-1
    for i in test_board:
        for j in i:
            if j>grt:
                grt=j
    return grt

def change():
    for i in range(n):
        for j in range(n):
            if board[i][j]=='G':
                board[i][j]='R'

n=int(input())
count=0
board=[]
for _ in range(n):
    board.append(list(input().strip()))

test_board=[[-1 for _ in range(n)]for _ in range(n)]


for i in range(n):
    for j in range(n):
        if test_board[i][j]==-1:
            navi(i,j)
            count+=1

not_weak=getmax()+1
count=0
change()
test_board=[[-1 for _ in range(n)]for _ in range(n)]

for i in range(n):
    for j in range(n):
        if test_board[i][j]==-1:
            navi(i,j)
            count+=1
weak=getmax()+1
print(not_weak,weak)
