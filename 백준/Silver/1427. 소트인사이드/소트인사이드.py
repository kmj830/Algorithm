def selection_sort(arr):
  l=len(arr)
  idx=0
  while idx<l-1:
    idx_max=idx
    for i in range(idx,l):
      if arr[idx_max]<=arr[i]:
        idx_max=i
    tmp=arr[idx]
    arr[idx]=arr[idx_max]
    arr[idx_max]=tmp
    idx+=1
  return arr


a=list(map(int,input()))
print(''.join(list(map(str,selection_sort(a)))))