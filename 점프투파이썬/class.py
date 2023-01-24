class FourCal:
    def __init__(self,first,second): # 생성자 : 초기 값 세팅
        self.first = first
        self.second = second
    def setdata(self,first,second): # 메서드의 매개변수
        self.first = first # 메서드의 수행문
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result= self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal(4,2)
b = FourCal(3,8)

print(a.add())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

class MoreFourcal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourcal(4,0)
print(a.pow())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second
a = SafeFourCal(4,0)
print(a.div())
