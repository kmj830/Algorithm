# 문제 4 / 구간 합 구하기 2
# https://www.acmicpc.net/problem/11660

import sys
input=sys.stdin.readline

# 입력

N,M=map(int,input().split())
table=[[0]*(N+1)]
for _ in range(N):
  table.append([0]+list(map(int,input().split())))

# 전처리
table_prcd=[[0 for _ in range(N+1)]for _ in range(N+1)]
for i in range(1,N+1):
  for j in range(1,N+1):
    table_prcd[i][j]=table_prcd[i-1][j]+table_prcd[i][j-1]-table_prcd[i-1][j-1]+table[i][j]

# 도출
for _ in range(M):
  x1,y1,x2,y2=map(int,input().split())
  print(table_prcd[x2][y2]-table_prcd[x1-1][y2]-table_prcd[x2][y1-1]+table_prcd[x1-1][y1-1])