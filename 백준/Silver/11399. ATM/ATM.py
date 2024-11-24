from sys import stdin
input=stdin.readline
def insertion_sort(arr):
  l=len(arr)
  for idx in range(1,l):
    find_idx=idx
    for i in range(idx-1,-1,-1):
      if arr[i]>arr[idx]:
        find_idx=i
    tmp=arr[idx]
    for i in range(idx-1,find_idx-1,-1):
      arr[i+1]=arr[i]
    arr[find_idx]=tmp
  return arr
    

n=int(input())
a=list(map(int,input().split()))
sorted_a=insertion_sort(a)
total=0;num=0
for i in sorted_a:
  num+=i
  total+=num
print(total)