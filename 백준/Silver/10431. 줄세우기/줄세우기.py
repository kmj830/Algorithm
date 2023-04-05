testcase=int(input())
count=[0 for _ in range(testcase)]
for i in range(testcase):
    student=[]
    tmp=input().split()
    tmp.remove(tmp[0])
    for j in range(20):
        if int(tmp[j]) in student:
            continue
        else:
            student.append(int(tmp[j]))
        if j==0:
            continue
        for k in range(len(student)):
            if k==0:
                continue
            if student[-k]<student[-k-1]:
                student[-k],student[-k-1]=student[-k-1],student[-k]
                count[i]+=1
for i in range(len(count)):
    print(i+1,count[i])