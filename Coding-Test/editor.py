from sllist import Linked_list #Linked_list 가져오기
# 입력 받기
data = input('문자열 입력: ')# 첫째줄에는 문자열이 주어진다. abcd 면
cursor = len(data) # 문자열의 갯수  4 , 커서는 맨뒤에 잇음!
second = int(input('명령어 갯수 : ')) # 둘째줄에는 명령어의 갯수가 주어진다.
command = [] # 셋째줄부터는 입력할 명령어가 순서대로 주어진다. 리스트에 넣는다.
command2 = int(input('명령어 입력'))
command.append(command2)
for i in range(len(command)): # 입력받은 값을 하나하나씩 반복한다.
    command2 = input().split() # 커멘드를 하나하나 나누기
    if 'L' in command: # L 명령어 입력 받으면 커서를 왼쪽으로 옮기기
        command2 = cursor.append() # 커서를 왼쪽으로 옮기기
    elif 'D' in command: # D 명령어 입력 받으면 커서를 오른쪽으로 한 칸 옮김
        command2 = command.popleft() # 커서를 왼쪽으로 옮기기
    elif 'B' in command: # 커서 왼쪽에 있는 문자를 삭제함
        command2 = command.pop(-1)
    elif 'P ' in command : #P$ 입력시
        command2 = command.split()[1]
        command2.append(command2)

print(command2)
