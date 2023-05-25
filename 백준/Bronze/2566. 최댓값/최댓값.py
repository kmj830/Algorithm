board=[];MaxOfLine=[]
for i in range(9):
    board.append(list(map(int,input().split())))
    MaxOfLine.append(max(board[i]))
print(max(MaxOfLine))
print(MaxOfLine.index(max(MaxOfLine))+1,board[MaxOfLine.index(max(MaxOfLine))].index(max(MaxOfLine))+1)