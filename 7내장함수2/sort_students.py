# # 스튜던트 라는 클래스를 만들고 Tostring이라는 함수를 이용해 intstance들을 출력해보자
# Student(self):
#   def __init__(self, name, ):
#     self.name = name
#     self. = 

#   def __string__(self):
#     self.name

# students = [
#   Studnet("김일수", 10),
#   Studnet("김이수", 20),
#   Studnet("김삼수", 30),

# ]   

# print(student[0])

# ========================================
# 정답 및 리뷰
# 1. 클래스 선언 주의!, init은 return이 없넹
# 2. format함수 사용 주의!
# 3. __str__ = Tostring
# ========================================

class Student:
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def __str__(self):
    return "{}:{}".format(self.name, self.score)

students = [
  Student("김일수", 10),
  Student("김이수", 20),
  Student("김삼수", 30)
]

print(students[0])

students = sorted(students, key= lambda stu: stu.score)
print_students()

students.sort(key= lambda stu: stu.score)
print_students()
