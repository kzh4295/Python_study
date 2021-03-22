# class Students:
#   def __init__(self, name, gender, age, score):
#     self.name = name
#     self.gender = gender
#     self.age = age
#     self.score = scrore

#   def __str__(self):

# with open students.csv as file:
#   sort_students = sorted(students, key = lambda stu: stu.score)

# ==============================================================
# 정답 및 리뷰
# 1. reduce, with open, sort, map 왜 생각못했지 ㅠㅠ..
# ==============================================================
from functools import reduce
from Student import Student
# import Student

g_grades = ['A', 'B', 'C', 'D', 'F']
g_grades.reverse()

students = []
with open('students.csv', 'r', encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0: continue
        students.append( Student(line) )

students.sort(key = lambda stu: stu.score, reverse = True)
m = map(lambda stu: stu.make_grade(), students)
list(m)

def sumfn(x, y):
    if type(x) == int:
        return x + y.score
    else:
        return x.score + y.score

# total = reduce(lambda x, y: (x if type(x) == int else x.score) + y.score, students)
total = reduce(sumfn, students)
avg = total / len(students)
print("총계, 평균>>>", total, avg)

print("이름\t성별\t나이\t학점")
print("----\t----\t----\t----")
for s in students:
    print(s)

print("-----------------------------")
for s in students:
    if s.score >= avg:
        print(s.name, s.score)

    