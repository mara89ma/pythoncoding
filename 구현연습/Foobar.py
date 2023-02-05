n = int(input("입력하세요"))
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0: #입력된 값이 3의 배수이고 5의 배수이면
        i = "FooBar" # i에 FooBar를 넣고
        print(i) # 출력
    elif i % 3 == 0: # 3의 배수이면?
        i = "Foo" # i에 Foo 넣고
        print(i) # Foo 출력
    elif i % 5 == 0 : # i가 5의 배수면?
        i = "Bar" # i에 Bar 넣고
        print(i) # i 출력
    else: # 그외에
        print(i) # 
