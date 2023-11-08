n=int(input())
temp=[]
result=[]
for i in range(n):
    temp.append(input())

for i in range(len(temp[0])):
    record={}
    now=''
    for j in range(len(temp)):
        now=temp[j][i]
        try:
            record[temp[j][i]]+=1
        except:
            record[temp[j][i]]=1
    if len(record)!=1:
        result.append('?')
    else:
        result.append(now)
print(''.join(result))