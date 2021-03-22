# import reduce from textTools

# product = 1
# list = [1, 2, 3, 4]
# for num in list:
#   return product = product * number 

# print("product1", product)

# print (reduce(lambda x x * y, list))
# print("product2", product2)

# ======================================
# 정답 및 리뷰
# 1. textTools(X)>>  functools(o)
# 2. for문과 return은 세트가 아니다.
# 3.  lambda가 한줄로 표현해서 깔끔하구나
# ========================================

from functools import reduce

lst = [1, 2, 3, 4]
product = lst[0]
for i , num in enumerate(lst):
  if i == 0: continue
  product = product + num
  print("product1", product)

  product2 = reduce(lambda x, y: x + y, lst)
  print("product2", product2)
