def snail(n):
    arr = [[0 for j in range(n)] for i in range(n)]
    drow = [0, 1, 0, -1] # 행 변화, 우하좌상, 행은 세로 축이므로, 상하 이동시 에만 변경 (상 : +1, 하 :-1)
    dcol = [1, 0, -1, 0] # 열 변화, 우하좌상, 열은 가로 축이므로, 좌우 이동시 에만 변경 (좌 : -1, 우 : +1)

    row, col = 0, 0 # 시작 행,열 정의
    dp = 0 # 방향 전환을 위한 값 0: 우, 1:하, 2:좌, 3:상
    for cnt in range(1, n * n + 1): #1부터 26까지
        arr[row][col] = cnt #arr[0][0] = 1
        next_row, next_col = row + drow[dp], col + dcol[dp] # next_row : 0+drow[0]=>0+0, next_col : 0+dcol[0]->1 => [0,1]
        if not (0 <= next_row < n and 0 <= next_col < n and arr[next_row][next_col] == 0): # 만약에 next_row가 0보다 크고 n(1)보다 작고, next_col이 0보다 크고 n(1)보다 작다, next_row는 조건을 충족 못하면
            dp = (dp + 1) % 4 # 왜 4 -> 방향 만약에 
            next_row, next_col = row + drow[dp], col + dcol[dp] # 다시 시작
        row, col = next_row, next_col
    return arr

print(snail(5))
