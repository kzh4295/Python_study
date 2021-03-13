# #  Dog 클래스 생성, 상태,소멸
# Class = Dog(self, name):
#   def __init__(self):
#     print("생성")

#   def speak(self):
#     self.name = 
#     print("wal")

#   def 

#   def __del__(self):
#     print("소멸")

# class puppy(Dog):
#   def __init__(self, name):
#     print(self.name,  "self.name 생성")

#   def wag(self):
#     print("puppy 왈왈")

# 자식에게만 생성된 것은 부모에서 출력했을때, 에러 발생!

# ==========================================
          정답
# ==========================================


#  Class(x)>>class(o)
class Dog:
  def __init__(self, name):
    self.name = name  
    self.color ="Blue"
    print(self.name, "was Born")
    print("$$$$$$$$$")

  def speak(self):
    print("yelp!", self.name)

  def __del__(self):
    print("destroy!!")

# 상속: 부모(Dog)의 습성을 가지고 있지만, 하단의 자식의 습성이 우선되어 instance 생성
class Puppy(Dog):
  name = "강아지"

  def __init__(self):
    self.name = "Puppy"
    self.color = "Red"
    print("QQQQ> Puppy was Born", self.name)

  def __read_diary(self):
    print("Diary content!!!")

  def speak(self):
    self.age = 234
    print("bow wow", self.name) 

  def wag(self):
    self.__read_diary() 
    print("puppy's wag tail")

  def tto():
    print("Ttoooooooo00000")

d = Dog("puddle")
p = Puppy()
d.speak()
p.speak()
# d.wag()
p.wag()

# p.__read_diary()

print("aaaaa", d.name, p.name )

