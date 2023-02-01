class Node: # 노드는 변수와 다음 값을 가리키는 값으로 구성되어 있다.
    def __init__(self, value=None, next_node=None): #노드를 만들고, 값과 다음 값을 초기화 시킨다.
        self.value = value # 값이 들어가는 변수 만들기
        self.next_node = next_node # 다음 값을 가르키는 변수(포인터) 만들기.

class LinkedList: # 링크드리스트를 클래스로 만들기
    def __init__(self): # 초기화
        self.head = None # 연결리스트의 시작 노드가 없음
        self.tail = None # 연결리스트의 끝 노드 없음
        self.current = None # 현재 값 노드가 없음

    def add(self, value): # 링크드리스트 : 현재 위치의 값을 추가하는 기능이 있음
        new_node = Node(value) # 추가해줄 새로운 노드를 노드 변수로 정의한다.
        if self.head is None: # 연결리스트의 시작노드가 없으면?
            self.head = new_node # 시작노드에 현재 노드 추가
            self.tail = new_node # 끝노드에 현재 노드 추가 < 한개로 구성되어 있는 리스트>
            self.current = new_node # 현재노드에 현재 노드 추가
        else: # 시작값이 있으면
            self.tail.next_node = new_node #끝 노드의 다음 노드(포인터)에 현재 노드 추가하기.
            self.tail = new_node # 끝노드에 현재 노드 (뉴 노드는 value와 next_node로 구성되어있고, next_node값은 None)추가하기

    def delete(self): # 현재 위치의 값을 삭제할 수 있는 기능이 있음
        if self.head is None: # 시작노드가 없으면?
            return None # none 리턴 (삭제할 값이 없음)
        if self.head == self.tail: # 시작노드와 끝노드가 같으면? 하나있다는 이야기
            value = self.head.value  # 값에 현재 시작노드의 값 넣기
            self.head = None # 시작노드  none 으로 변경하기(제거)
            self.tail = None # 끝노드  none으로 변경하기 (제거)
            self.current = None # 현재노드 none으로 변경하기(제거)
            return value

        if self.current == self.head: # 현재노드가 첫번째 노드 값이라면?
            value = self.head.value # 값에 현재 노드 값 넣기
            self.head = self.head.next_node # 첫번째 노드 값에 다음 노드 값 넣기 (첫번째가 삭제되었으니까)
            self.current = self.head # 현재값이 첫번째 노드값이 된다.(삭제되고, 두번째였던 노드값을 가리킴)
            return value

        else: # 그외에는(리스트가 하나가 아니고, 삭제할 노드가 첫번째 노드가 아님 적어도 두번째 노드임)
            previous = self.head # previous라는 변수에 첫번째 노드값이라고 정의
            while previous.next_node != self.current: # 첫번째 노드 값이 현재 찾는값과 같지 않다면 ?
                previous = previous.next_node # previous 변수에 현재 다음 노드를 정의함.
                # 같을때 까지 반복, 같으면 나옴
            value = self.current.value # 찾은 값을 현재 벨유 값에 넣음 -> 삭제
            previous.next_node = self.current.next_node # 다음노드의 값은 현재노드의 값과 음
            if self.current == self.tail: # 찾는 값이 마지막 값이라면?
                self.tail = previous # 마지막노드값을 previous 변수에 추가
                self.current = self.current.next_node # 현재노드 값은 현재노드값으 ㅣ다음 노드값(none)과 같음
                return value

    def get(self): #현재 값을 가져올 수 있다.
        if self.current: #  현재값
            return self.current.value # 현쟈 값의 데이터값 리턴
        else: # 그외(링크드리스트의 값이 없음)
            return None #  none 리턴

    def move_next(self): # 다음 위치로 이동하느느 기능이 있다.
        if self.current: # 현재값이라면 ?
            self.current = self.current.next_node # 현재값의 다음노드 값으로 정의하고 다음 노드값을 출력한다.


    def move_front(self): # 앞으로 가기
        self.current = self.head # 현재값을 첫번째 노드 값으로 정의하고 첫번째 노드값을 출력한다.

L = LinkedList()
L.add(1)
L.add(2)
L.add(3)
print(L.get())
L.move_next()
print(L.get())
L.delete()
L.move_front()
print(L.get())
L.move_next()
print(L.get()) # 1ㄷㅏ음에 2여야되는데, 2지웟고 그담은 3임
