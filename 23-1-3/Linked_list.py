class LinkedList:
    def move_next(self):  # 다음 값으로 이동하기, 포인터의 노드에 다음 노드의 주소값이 잇음
        return self.pointer
        pass
    def get(self): #  값을 구하기
        return self.value #  해당값의 원래 값
        pass
    def add(self, value): # 값을 추가하기
        self.pointer = self.value
        return self.value
        pass
    def delete(self): # 값 삭제하면 포인터가 삭제됨
        self.pointer = None
        return None
        pass
    def move_front(self): # 맨처음으로 이동
        if self.length == 0:
            return None
        return self
        pass
    def __init__(self,value=None,pointer=None): # 리스트는 값과 포인터를 가짐
        self.value = value
        self.pointer = pointer
        pass


List2 = [5,4,3,2,1]
LinkedList.get(Link)
