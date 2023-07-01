arr=input()
temp=set()
for i in range(len(arr)):
    for j in range(i,len(arr)+1):
        temp.add(arr[i:j])
temp.discard('')
print(len(temp))