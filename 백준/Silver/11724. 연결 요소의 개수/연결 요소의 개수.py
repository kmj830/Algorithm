import sys
input=sys.stdin.readline
n,m=map(int,input().split())
adjacency_list={i:[] for i in range(1,n+1)}
for _ in range(m):
    u,v=map(int,input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)
visits_list=[True]+[False for _ in range(n)]
stack=[]
probe_sequence=[]
count=0
for i in range(1,n+1):
    if visits_list[i]==False:
        count+=1
        visits_list[i]=True
        stack.append(i)
        while stack:
            node=stack.pop()
            for adjacency_node in adjacency_list[node]:
                if visits_list[adjacency_node]==False:
                    stack.append(adjacency_node)
                    visits_list[adjacency_node]=True
            probe_sequence.append(node)
print(count)