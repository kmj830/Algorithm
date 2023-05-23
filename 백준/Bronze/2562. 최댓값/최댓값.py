maxnum=0;maxindex=0
for i in range(9):
    newnum=int(input())
    if newnum>maxnum:
        maxnum=newnum
        maxindex=i+1
print(maxnum)
print(maxindex)