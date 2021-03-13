# list, dic, enumerate
# lst = ['오렌지', '사과', '배']
# dic = {'오렌지': 400, '사과': 200, '배': 300}

# for key in dic:
#   print("key=", key, dic[key])

# print(list(enumerate(lst)))

# for i, value in enumerate(lst):
#   print("tt =" , i, value)

# for key, element in dic.items():
#   print("items.key= ", ", element=", element)


for i in range(0, 20, 2):
  print(i)
  i = i ** 2

# 반복문의 간결한 표현
arr = [i ** 2 for i in range(0, 20 , 2)]
print(arr)

#  최대값, 최소값
print("최소값", min(arr))
print("최대값", max(arr))

lst = ["사과", "배"]
outs = [f for f in lst if f!= '사과']
print(outs)

# input : 터미널에서 입력을 받음
cmd = input("Input>>")
print(cmd)

cmds = cmd.split('')
print(cmds)