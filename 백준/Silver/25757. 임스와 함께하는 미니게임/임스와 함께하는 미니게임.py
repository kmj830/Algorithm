import sys
nop,n=input().split();people=[]
match n:
    case "Y":
        n=int(2)
    case "F":
        n=int(3)
    case "O":
        n=int(4)
for i in range(int(nop)):
    people.append(sys.stdin.readline().rstrip())
print(len(list(set(people)))//(int(n)-1))