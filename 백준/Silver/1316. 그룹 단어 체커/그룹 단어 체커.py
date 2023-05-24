N=int(input());count=N
for i in range(N):
    word=input()
    charlist=[]
    charlist.append(word[0])
    for i in range(1,len(word)):
        if word[i]!=word[i-1]:
            if charlist.count(word[i])!=0:
                count-=1
                break
            else:
                charlist.append(word[i])
print(count)