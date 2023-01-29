# que는 맨 먼저 줄 선 사람이 먼저 서비스를 받는다.
class Que:
    def __init__(self):
        self.data = []
    def push(self, value):
        self.data.append(value)
    def pop(self): # 처음 넣은 값 삭제,,
        self.data.pop(0)

# TEST
Q = Que()
Q.push(1)
Q.push(2)
Q.push(3)
print(Q.data)
Q.pop()
print(Q.data)
