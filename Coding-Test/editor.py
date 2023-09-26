from sllist import Linked_list
editor = Linked_list()
data = int(input())
for i in range(data):
    command = input().split() # 커멘드를 하나하나 나누기
    if 'L' in command: # L 명령어 입력 받으면 커서를 왼쪽으로 옮기기 -> POPLEFT 사용
        command = editor.popleft() # 커서를 왼쪽으로 옮기기
    elif 'D' in command: # D 명령어 입력 받으면 커서를 오른쪽으로 한 칸 옮김
        command = editor.popleft() # 커서를 왼쪽으로 옮기기
    elif 'B' in command: # 커서 왼쪽에 있는 문자를 삭제함
        editor.popleft()
    else :# P$라는 문자를 커서 왼쪽에 추가함
        editor.append('$')
