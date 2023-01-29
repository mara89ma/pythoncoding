# 스택은 마지막에 삽입한 데이터를 가장 먼저 사용 한다.
# 나중에 들어간 데이터가 젤 먼저 나오는 방식
# 들어오고 나오는 방식 거꾸로

class Stack: #스택 클래스를 정의한다.
    def __init__(self):
        self.data = [] # 데이터를 리스트로 정의해준다.
    def push(self, value):
        self.data.append(value) # append() 맨 마지막에 값을 추가한다.
    def pop(self):
        self.data.pop() # pop()은 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제

# TEST
S = Stack()
S.push(12)
S.push(13)
print(S.data)
S.pop()
print(S.data)
