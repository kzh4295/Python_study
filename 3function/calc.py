# # 두 수를 받아, 사칙 연산 수행 함수
# # +
# def plus(a, b):
#   return a + b 

# # -
# def minus(a, b):
#   return a - b

# # *
# def minus(a, b):
#   return a * b

# # /
# def minus(a, b):
#   return a / b   

# # 정답
# # +
# def plus(a, b):
#   return a + b 

# # -
# def minus(a, b):
#   return a - b

# # *
# def mul(a, b):
#   return a * b

# # /
# def div(a, b):
#   if b == 0:
#     return a 

#   return a / b   

# ToDo cmds 하나만으로 set해보기!
cmd = input("수식을 입력하세요(usage: 2 + 3)>")
cmds = cmd.split('')

a, op, b = int(cmds[0], cmds[1], int(cmds[2]))

if op == '+':
  r = plus(a, b)

elif op == '-':
  r = minus(a, b)

elif op == '*':
  r = mul(a, b) 

else:
  r = div(a, b)   

print("Answer is {:d}".format(r))