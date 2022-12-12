def seperate(n):
    sum = 0
    while n>0:
        for i in range(n):
            print(n)
            sum += n
            n -= 1
    print(sum)
    return seperate(1023)