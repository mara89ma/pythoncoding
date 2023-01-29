# 클래스

- 함수가 여러개 일때 , 전역 변수를 계속 추가하기 어려움
- 클래스 : 틀, 객체 : 틀을 이용해 만든 것
- 객체마다 고유한 성격을 가지는 것이 특징임, 동일한 클래스로 만든 객체들은 서로 영향을 주지 않음
- 객체, 인스턴스
- 클래스로 만든 객체 → 인스턴스
- 클래스 안에 구현된 함수 :  메서드

```python
def 함수명(매개변수):
	수행할 문장
```

- 메서드 첫 번째 매개변수 이름 : self 사용
- 객체 호출시 호출한 객체 자신이 전달되기 때문에 self라는 이름을 사용

## 어트리뷰트

- 클래스 내부에 포함되어 있는 함수, 변수

인스턴스 

- 클래스에 의해 만들어진 객체

매서드

- 객체에 포함되어 있는 함수

```python
class Dog : 
	kind ='cannie'
	def __init__(
```

```python
class Dog:
        def __init__(self,name):
                self.name = name
                self.tricks=[]
        def add_trick(self,trick):
                self.tricks.append(trick)

d = Dog("Fido")
e = Dog("Buddy")
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)
```

→ 각자 입력됨

```python
class Warehouse:
        purpose = 'storage'
	        region = 'west' # 클래스 변수
w1 = Warehouse()
print(w1.purpose,w1.region)

w2 = Warehouse()
w2.region = 'east' # 인스턴스 변수
print(w2.purpose,w2.region)
```

→ 인스턴스, 클래스 모두에서 같은 어트리뷰트 등장시, 어트리뷰트 조회는 인스턴스 우선

클래스 연습

```python
class FourCal:
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
a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,8)
print(a.add())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
```

생성자 : 클래스의 초기값을 세팅하는 과정

클래스의 상속 : 다른 클래스의 기능을 물려받음

- 메서드 오버라이딩 : 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것

클래스 변수 : 클래스로 만든 모든 객체에 공유되는 특징을 가짐
