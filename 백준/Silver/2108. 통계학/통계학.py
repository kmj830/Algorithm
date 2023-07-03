import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
print(round(sum(arr)/n))
print(sorted(arr)[n//2])
count={i:0 for i in arr}
for i in arr:
    count[i]+=1
count=[*count.items()]
count.sort(key=lambda x:x[1])
new_count=[[i,j] for i,j in count if j==count[-1][1]]
new_count.sort(key=lambda x:x[0])
if len(new_count)>1:
    print(new_count[1][0])
else:
    print(new_count[0][0])
print(max(arr)-min(arr))