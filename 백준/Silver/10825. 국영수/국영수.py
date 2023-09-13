n=int(input())
students={}
for _ in range(n):
    student,*scores=input().split()
    scores=list(map(int,scores))
    students[student]=scores
sortedbygrade=sorted(students.items(),key=lambda x:(-x[1][0],x[1][1],-x[1][2],x[0]))
for i in sortedbygrade:
    print(i[0])