# # 선언
# def fn(): 
#   print("fn called") #input과 output이 없고 단지 부를뿐

# # 메모리에 올림(인터프리터언어는 선언하고 부를때 메모리에 올라감 )
# fn() 

# #input 과 output이 있음
# def exp(x):
#   return x ** 2 

# # 변수는 언더바(_), 숫자, 영문으로 가능
# exp3 = exp(3)
# print(exp3)
# print(exp(9))

# # 리스트 형태 출력
# def get_fruits():
#   return['오', '사', '바나나']
# print( get_fruits()[1] )

# # #튜플은 할당 불가능
# def get_name():
#   return "kent", 'back'

# name = get_name()
# name[1] = "aaa"
# print( name ) 

# def full_name(first_name, last_name):
#   return first_name + '' + last_name

# name = get_name()
# print( name, full_name('AAA', 'BBB')) 

def var_param(a, *vp):
  print(a, len(vp), vp[len(vp) -1])
  print(type(vp))
var_param("AA", 'bbb', 'ccc')  #bbb, ccc는 튜플

def default_param(a, b):
  print(a, b)

default_param("aaa")
default_param("aaa", 'bbbbb')


