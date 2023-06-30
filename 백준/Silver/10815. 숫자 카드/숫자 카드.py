import sys
n=int(sys.stdin.readline().strip())
n_nums=set(list(map(int,sys.stdin.readline().split())))
m=int(sys.stdin.readline().strip())
m_nums=list(map(int,sys.stdin.readline().split()))
intersection=(n_nums.intersection(set(m_nums)))
for i in m_nums:
    print(1,end=" ") if i in intersection else print(0,end=" ")