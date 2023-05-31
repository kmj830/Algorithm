N=int(input())
numbers=list(map(int,input().split()));notdecimal=[]
for num in numbers:
    if num==1:
        notdecimal.append(num)
        continue
    for i in range(2,num):
        if num%i==0:
            notdecimal.append(num)
            break
for num in notdecimal:
    if num in numbers:
        numbers.remove(num)
print(len(numbers))