n = 26 #입력받는 변수
num = n # num은 바뀌어서 계싼해야되서 변수로 둠
cnt = 0 # cnt는 몇번 반복했는지 나타내는 변수
while True:
    a = num//10 # a는 num의 첫번째 수
    b = num%10 # b는 num의 두번째 수
    c = (a+b)%10 # c는 a와 b를 더한 값의 두번째 수
    num = (b*10)+c #num은 나머지 수가 0.x니까 10을 곱하고 c를 더함

    cnt = cnt+1 # 반복 횟수를 위해서 더함
    if(num == n): # num의 값이 맨처음에 입력받은 변수와 같다면 멈추기
        break
print(cnt)
