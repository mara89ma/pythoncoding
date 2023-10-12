# Linked_list 가져오기
class Linked_list :
    #현재 값에 값을 추가하기 -> P
    #현재 값에 값을 삭제하기 -> B
    #현재 값에서 이전 값 으로 이동하기 -> L
    #현재 값에서 다음 값으로 이동하기 -> D

    class Node :
        def __init__(self,prev,next,value):
            self.prev = prev
            self.next = next
            self.value = value

    def get(self): # 모든 값 출력
        current = self.head
        value = ''
        while True:
            current = current.next
            if current is None:
                break
            value = value + current.value
        return value

    def insert(self, data): # P
        # 1. X -> Y -> Z
        #         ^
        #    X -> Y -> A -> Z
        #              ^
        X = self.current.prev
        Y = self.current
        Z = self.current.next

        A = Linked_list.Node(Y,Z,data)
        Y.next = A
        if Z is not None:
            Z.prev = A
        self.current = A #경 커서 변
        # 2.
        # X -> Y
        #      ^
        # X -> Y -> A
        #           ^

        #3.
        # Y -> Z
        # ^
        # Y -> A -> Z

    def remove(self): # B
        # 1. ç
                # ^
        #    X -> Z
        #    ^
        if self.current.value is None :        #3.  Y -> Z -> 삭제 안됨 -> x
            return
        X = self.current.prev
        Z = self.current.next

        X.next = Z
        if Z is not None:
            Z.prev = X
        self.current = X

        #2.
        #X -> Y
        #     ^
        #X
        #^

        #3.
        # Y -> Z
        # ^
        # 삭제 안됨 -> x

    def prev_move(self): #L 현재 값에서 이전 값 으로 이동하기
        if self.current.prev is None:
            return
        self.current = self.current.prev

    def next_move(self): #D 현재 값에서 다음 값으로 이동하기
        if self.current.next is None:
            return
        self.current = self.current.next

    def __init__(self,data):
        self.head = Linked_list.Node(None,None,None)
        self.current = self.head #현재 위치 = 맨 앞
        for i in data :
            self.insert(i)

data = input()# 입력 받기
command_count = int(input())# 둘째줄에는 명령어의 갯수가 주어진다.
data_list = Linked_list(data)
for i in range(command_count):# 셋째줄부터는 입력할 명령어가 순서대로 주어진다.
    command = input() # 입력받은 값을 하나하나씩 반복한다.
    if command[0] == "L" :# L 명령어 입력 받으면 커서를 왼쪽으로 옮기기
        data_list.prev_move()
    elif command[0] == "P" : # P$ 입력시 문자를 커서 왼쪽에 추가
        data_list.insert(command[2])
    elif command[0] == "D" : # D 명령어 입력 받으면 커서를 오른쪽으로 한 칸 옮김
        data_list.next_move()
    elif command[0] == "B" : # 커서 왼쪽에 있는 문자를 삭제함
        data_list.remove()

print(data_list.get()) # 모든 값 출력

# abcd
# 3
# P x
# L
# P y
