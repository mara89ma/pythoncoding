def solution(n):
    for i in range(2,n): # n의 제한사항 넣기,
        x = n%i
        if x == 1 : #나머지가 1이라면
            return i
