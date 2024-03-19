#반지름을 입력받아서, 원의 둘레와 원의 면적을 출력하는 프로그램

import math
pi=math.pi
r= int(input("반지름을 입력하시오"))
#면적 소수점 2번째
area= pi *r**2
#둘레 소수점 1번째
circumference=2*pi*r
print("반지름이 {}일때, 원의 면적는 {:.2f}이고, 원의 둘레는 {:.1f}입니다" .format(r,area,circumference))