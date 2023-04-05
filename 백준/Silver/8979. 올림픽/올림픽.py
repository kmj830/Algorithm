import sys
n,k=map(int,input().split())
nation={};j=1;count=0
for i in range(n):
    text=list(map(int,sys.stdin.readline().split()))
    extractkeyintext=str(text[1])+str(text[2])+str(text[3])
    nation.update({text[0]:extractkeyintext})
sortednation=sorted(nation.items(),key= lambda item: item[1],reverse=True)
for i in range(n):
    if sortednation[i][0]==k:
        count=i
        if count==0:
            print(count+1)
            break
        while sortednation[count][1]==sortednation[count-1][1]:
            count-=1
        print(count+1)
        break
    else:
        j+=1