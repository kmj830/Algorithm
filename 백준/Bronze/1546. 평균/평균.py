# 문제 2 / 평균 구하기
# https://www.acmicpc.net/problem/1546

N=int(input())
grade = list(map(int,input().split()))
top_grade = max(grade)
answer=0
for i in grade:
  answer+= i/top_grade*100
print(answer/N)