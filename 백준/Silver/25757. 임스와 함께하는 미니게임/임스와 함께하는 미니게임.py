nop,n=input().split();people=[]
match n:
    case "Y":
        n=int(2)
    case "F":
        n=int(3)
    case "O":
        n=int(4)
for i in range(int(nop)):
    people.append(input())
people=list(set(people))
print(len(people)//(n-1))