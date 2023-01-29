class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
        def __init__(self):
                init = Node('init')
                self.head = init
                self.tail = init
                self.현재노드 = None
                self.데이터수 = 0

        def __len__(self): # 길이를 출력할 수 있
                return self.데이터수
        def __str__(self):
                현재노드 = self.head
                현재노드 = 현재노드.next
                s = ''
                for i in range(self.데이터수):
                        s+= f'{현재노드.data},'# 현재 노드의 데이터
                        현재노드 = 현재노드.next #데이터가 들어있는만큼 순회
                return f'[{s[:-2]}]' # 앞뒤로 리스트처럼 대괄호처럼 , 마지막 , 스페이스를 없애줌


        def append(self,data):
                새로운노드 = Node(data) # 데이터가 새로 들어왔을 때 선
                self.tail.next = 새로운노드 # 마지막 노드에 넥스트값이 none인데 새로운 노드로 만들어 주겠다.
                self.tail = 새로운노드 # 새로운 노드가 됨
                self.데이터수 +=1 # 데이터수가 하나 새로 들어
        def insert(self, input_index, input_data):
            현재노드 = self.head

            for i in range(input_index):
                현재노드 = 현재노드.next
            신규노드 = Node(input_data)
            신규노드.next = 현재노드.next
            현재노드.next = 신규노드
            self.데이터수 += 1
        def pop(self):# 마지막값을 꺼내는것
                마지막값 = self.tail.data# 마지막값을 꺼내고,
                현재노드 = self.head # 없애줌줌
                for i in range(self.데이터수):
                    if 현재노드.next is self.tail:
                        self.tail = 현재노드
                        break
                    현재노드 = 현재노드.next #계속 순회해야되니까,
                self.데이터수 -= 1
                return 마지막값
        def find(self,data):
            index = -1 #init노드가 맨앞에 있기 때문에
            현재노드 = self.head

            for i in range(self.데이터수+1):# init노드가 있어서
                if 현재노드.data == data:
                    return index
                index += 1
                현재노드 = 현재노드.next # 순회
            return -1

l= LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(15)

# print(l.head.data)# 첫번째 head의 data 출력 -> init의 data : init
# print(l.head.next.data) # 첫번째 head의 다음 노드가 생성됨(10)다음 노드의 데이터 출력 -> 10
# print(l.head.next.next.data) # 10 다음 노드 데이터 출력 -> 20
#
#
# print(l.tail.data)
# print(len(l))
print(l.pop())
print(l)
print(l.find(50))
