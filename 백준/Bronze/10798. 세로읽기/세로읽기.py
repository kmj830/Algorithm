board=[]
for _ in range(5):
    board.append(list(input()))
for i in range(15):
    for j in range(5):
        try:
            print(board[j][i],end="")
        except:
            pass