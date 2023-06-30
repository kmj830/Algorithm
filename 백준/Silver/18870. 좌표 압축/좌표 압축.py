n=int(input())
array=list(map(int,input().split()))
temp=sorted(list(set(array)))
dic={temp[i]:i for i in range(len(temp))}
for i in array:
    print(dic[i],end=" ")