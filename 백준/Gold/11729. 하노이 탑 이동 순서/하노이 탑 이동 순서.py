def hanoi(n,start,end):
    if n==1:
        print(start,end)
        return
    hanoi(n-1,start,6-start-end) # n-1개의 원판들을 스타트 지점에서 경유지로 옮겨버림.
    print(start,end) # 가장 큰 원판 옮기기 출력
    hanoi(n-1,6-start-end,end) # 경유지에 있는 남은 원판들 종착지로 옮기기 실행

N=int(input())
print(2**N-1)
hanoi(N,1,3)