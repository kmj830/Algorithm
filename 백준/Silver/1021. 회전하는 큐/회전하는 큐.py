from collections import deque
n,m=map(int,input().split())
nums=deque([i for i in range(1,n+1)])
target=list(map(int,input().split()))
count=0
for i in target:
    while True:
        if i == nums[0]:
            nums.popleft()
            break
        else:
            if len(nums)/2>=nums.index(i):
                nums.rotate(-1)
                count+=1
            else:
                nums.rotate(1)
                count+=1
print(count)