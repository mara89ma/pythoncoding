from sllist import Linked_list #Linked_list 가져오기
# 입력 받기
data = input('문자열 입력: ')# 첫째줄에는 문자열이 주어진다. abcd 면
data = Linked_list()
cursor = len(data) # 문자열의 갯수  4 , 커서는 맨뒤에 잇음!
second = int(input('명령어 갯수 : ')) # 둘째줄에는 명령어의 갯수가 주어진다.
result = [] # 셋째줄부터는 입력할 명령어가 순서대로 주어진다. 리스트에 넣는다.
command = input('명령어 입력')
for i in range(len(command)): # 입력받은 값을 하나하나씩 반복한다.
    command = input().split() # 커멘드를 하나하나 나누기
    if 'L' in command: # L 명령어 입력 받으면 커서를 왼쪽으로 옮기기
        cursor = len(data)-1 # 커서를 왼쪽으로 옮기기, 커서의 갯수 -1
    elif 'D' in command: # D 명령어 입력 받으면 커서를 오른쪽으로 한 칸 옮김
        cursor = len(data)+1 # 커서를 오른쪽으로 옮기기
    elif 'B' in command: # 커서 왼쪽에 있는 문자를 삭제함
        command = cursor.pop()
    elif 'P ' in command : #P$ 입력시
        command = command[1]
        command.append(result)
print(command)
print(cursor)
