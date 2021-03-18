class TestClass:
  name = "TEST"

  def __init__(self):
    print("TTTTTTTTTTTTTTTTTT")

  # 인스턴스가 부르든 클래스가 부르든 편하게 불러도 된다
  @staticmethod
  def static_method():
    print("STATIC!!")

  # @property : 메서드에서 프로퍼티로 변경됨
  @property
  def full_name(self):
    return self.name + "ffff"

  def get_name(self):
    print("QQQQQQQQQQQQQQQQQQQQQ")
    return self.name

  def area(self, x, y):
    return x * y


class Child(TestClass):
  def get_name(self):
    super().get_name()
    return "Child Name:" + self.name

# 부모의 로직은 동일하게 적용하고 자식의 로직은 첨가할때 사용
  def area(self, x, y):
    t = super().area(x, y)
    return t / 2

#  test 는 인스턴스 >> test는 object
test = TestClass() 
child = Child()

# test.static_method()
TestClass.static_method()

# full_name이 메서드에서 프러퍼티(멤버변수)이므로 괄호 생략됨
print("ffffffff>>>>", test.full_name)


# test에서 get_name을 불러오는 함수
getattr(test, 'get_name')()
getattr(TestClass, 'static_method')()

print("11111>>", child.get_name())    

c = callable(test.get_name)
print("ccccccc>>", c)