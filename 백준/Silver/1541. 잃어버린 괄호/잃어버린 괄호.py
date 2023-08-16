import sys
input=sys.stdin.readline
formula=input().strip().split('-')
for i in range(len(formula)):
    formula[i]=str(sum(list(map(int,formula[i].split('+')))))
print(eval('-'.join(formula)))