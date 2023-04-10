import sys
n=int(input())
board=[[0 for _ in range(n)]for _ in range(n)]


for i in range(n):
    board[i]=sys.stdin.readline().strip()

for i in range(n):
    if "*" in board[i]:
        for j in range(n):
            if board[i][j]=="*":
                head=[i,j]
                heart=[head[0]+1,head[1]]
                print(heart[0]+1,heart[1]+1)
                break
        break
leftarm=0
for i in range(heart[1]):
    if board[heart[0]][i]=="*":
        leftarm+=1
print(leftarm,end=" ")
rightarm=0
for i in range(n-heart[1]-1):
    if board[heart[0]][heart[1]+1+i]=="*":
        rightarm+=1
print(rightarm,end=" ")
waist=0
for i in range(n-heart[0]-1):
    if board[heart[0]+1+i][heart[1]]=="*":
        waist+=1
print(waist,end=" ")
leftleg=0
for i in range(n-heart[0]-waist-1):
    if board[heart[0]+waist+1+i][heart[1]-1]=="*":
        leftleg+=1
print(leftleg,end=" ")
rightleg=0
for i in range(n-heart[0]-waist-1):
    if board[heart[0]+waist+1+i][heart[1]+1]=="*":
        rightleg+=1
print(rightleg,end=" ")