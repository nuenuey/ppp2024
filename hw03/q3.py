#과제02-3 수정// 원의 넓이, ex) r=4

import math
pi=math.pi
r= int(input("반지름을 입력하시오"))
area= pi *r**2
print("반지름이 {}일때, 원의 넓이는 {}입니다" .format(r,area))