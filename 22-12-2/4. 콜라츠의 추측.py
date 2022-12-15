n = int(input("입력하세요"))
c = 0
for i in range(500):
    if n % 2 == 0: # i가 짝수 이면
        n = n/2 # i는 i를 2로 나눈 값
        c = c + 1 # 이 구문이 실행 되면 c에 1을 더함
    if n ==1:
        break
    if n % 2 == 1 : # i가 홀수이면
        n = (3*n) + 1 # 3을 곱하고 1을 더한이 i가 된다.
        c = c + 1 # 이 구문이 실행 되면 c에 1을 더한다.
    if n == 1:
        break
    if n >500 and n != 1:
        c = -1
        break
print(c)
