class Array:
    def get(self, idx): #특정 값을 리턴하는 함수, 자료마다 인덱스가 있어서 그 인덱스를 찾으면 해당 자료로 갈 수 있음
        return self.array2[idx]
    def set(self, idx, value): # 특정 인덱스의 값을 수정하는 함수,자료마다 인덱스가 있어서 수정할때 해당 인덱스로 가서 수정한다.
        self.array2[idx] = value
    def __init__(self, size): # 배열을 주어진 크기로 초기화 하기
	      self.array2 = [0]*size	
