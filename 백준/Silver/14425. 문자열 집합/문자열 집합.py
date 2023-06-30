import sys
n,m=map(int,sys.stdin.readline().split())
n_words=[sys.stdin.readline().strip() for i in range(n)]
m_words=[sys.stdin.readline().strip() for i in range(m)]
intersection=list(set(n_words).intersection(m_words))
count=0
for i in intersection:
    count+=m_words.count(i)
print(count)