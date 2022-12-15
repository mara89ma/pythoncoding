n  = int(input("입력하세요"))
# n>=1 and n<=50
for i in range(1,n+1): # 1부터 n까지 출력
    # print(i)
    if i % 3 == 0 and i % 5 == 0: # 만약 i가 3의 배수이고 5의 배수면 "FooBar" 출력
        n = "FooBar"
        print(n)
    elif i % 3 == 0: # 둘다 아니고 3의 배수면
        i = "Foo" # Foo 출력
        print(n)
    elif i % 5 ==0: # 둘다 아니고 5의 배수면
        i = "Bar" # Bar 출력
        print(n)
    else: # 다 아니면 ? 그냥 숫자 출력
        print(n)

