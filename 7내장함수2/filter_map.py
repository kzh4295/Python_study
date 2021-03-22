# # filter함수와 map 함수의 사용 비교
# filter( "filter", lamda : x x>0 ,iter()):
# map("map", lambda: x x < 0, iter()):

# ==================================
# 정답 및 리뷰: 
# 1. 변수 정리를 잘하자
# 2. lambda x:형태다
# 3. 출력할땐 list 형태로 해야하나 보다?
# ==================================

int_numbers = range(-5, 6)
f = filter (lambda x: x * 2, int_numbers)
m = map(lambda x: x * 2, int_numbers)

print("f=", list(f))
print("m=", list(m))

