i = int(input("입력하세요"))
c = 0
# for i in range(N):
while i == 1: # i가 1일때 까지 반복
    if i % 2 == 0: # i가 짝수 이면
        i = i/2 # i는 i를 2로 나눈 값
        c = c + 1 # 이 구문이 실행 되면 c에 1을 더함
    elif i % 2 == 1 : # i가 홀수이면
        i = (3*i) + 1 # 3을 곱하고 1을 더한이 i가 된다.
        c = c + 1 # 이 구문이 실행 되면 c에 1을 더한다.
print(c)
