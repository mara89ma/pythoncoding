def solution(arr):
    answer = 0
    count = 0
    for i in arr:
        answer = answer + i
        print(answer)
        count += 1         # i:1/c:1/a:1, i:2/c:2/a:3, 
                            # i:3/c:3/a:5 ,i:4/c:4/a:8
    answer = answer/count  # 8/5
    return answer
