def SwapNum(a):
    if input_switch[a]==0:
        input_switch[a]=1
    else:
        input_switch[a]=0
    return

switchnum=int(input())
input_switch=[-1]+list(map(int,input().split()))
studentnum=int(input())
for i in range(studentnum):
    sex,num=list(map(int,input().split()))
    if sex==1:
        for j in range(num,switchnum+1,num):
            SwapNum(j)
    else:
        SwapNum(num)
        for j in range(switchnum//2):
            if num+j>switchnum or num+j<1: break
            if input_switch[num-j]==input_switch[num+j]:
                SwapNum(num-j)
                SwapNum(num+j)
            else:
                break
for i in range(1,switchnum+1):
    print(input_switch[i],end=" ")
    if (i)%20==0:
        print()