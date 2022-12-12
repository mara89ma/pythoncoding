def snail(n):
    arr = [[0 for j in range(n)] for i in range(n)] #1
    row = 0 #2 행
    col = -1 #2 열
    cnt = 1 #3
    trans = 1 #4
    while n > 0: #5
        for i in range(n): #6
            col += trans # 열을 하나씩 추가
            arr[row][col] = cnt # arr[0][0] = 1
            cnt += 1  # cnt => 1+1 => 2
        n -= 1 #7
        for j in range(n): #8
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1 #9 # trans => 1*1 => -1
    return arr

print(snail(4))
