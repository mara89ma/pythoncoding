dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)): # a의 길이만큼 반복하여 j 에 넣어서 하나씩 비교
    for i in dial:
        if a[j] in i: #위에 있는  dial 에 맞는 결과값이 있으면 출력력
           ret += dial.index(i)+3
print(ret)
