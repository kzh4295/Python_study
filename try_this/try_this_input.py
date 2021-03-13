# # 자체 풀이
# a = input("이름")
# b = input("나이")
# c = input("성별")

# print("당신의 이름은",  {},"나이는",  {}, "성별은", {} .format(a, b, c ), "입니다.")

#  정답
cmd = input ("Input(usage: 이름,나이,성별) >> ")
print("aaa="+ cmd + ".")

error_msg = "정확히 입력해 주세요!"

if cmd.find(',') == -1: # find = -1 값이 없음
  print(error_msg)      # 들여쓰기 주의하자
  exit()

isExistsComma = False
for i in cmd:
  if i == ',':
    isExistsComma = True
    break

# validation?   if isExistsComma == False:
  print(error_msg)
  exit()

cmds = cmd.split(',')
outmsg = "당신의 이름은 {}, 나이는 {}, 성별은{} 입니다."
print(outmsg.format(cmds[0], cmds[1], cmds[2]))
