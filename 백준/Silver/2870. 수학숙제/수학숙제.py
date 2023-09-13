import re
N=int(input())
nums=[]
for _ in range(N):
    temp=re.findall('\d+',input())
    for num in temp:
        nums.append(int(num))
nums.sort()
for i in nums:
    print(i)