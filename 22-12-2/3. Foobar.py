n  = int(input("입력하세요"))
# n>=1 and n<=50
for i in range(1,n+1): # 1부터 n까지 출력
    # print(i)
    if i % 3 == 0  and i % 5 == 0:
        i = "FooBar"
        print(i)
    elif i % 3 == 0:
        i = "Foo"
        print(i)

    elif i % 5 == 0 :
        i = "Bar"
        print(i)
    else:
        print(i)
