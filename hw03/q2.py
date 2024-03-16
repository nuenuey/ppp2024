#실습 2 //ex) 키= 170cm, 몸무게= 60

height_cm= int(input("키를 입력하시오"))
weight=int(input("몸무게를 입력하시오"))
height_m =height_cm/100

bmi=weight/(height_m*height_m)
print("키가 {}cm, 몸무게가 {}이면, bmi는 {}입니다".format(height_cm,weight,bmi))

#실습 3 수정 // import math 사용
#pow(): 거듭제곱을 계산하는 함수__pow(밑,지수)
import math
height_cm= int(input("키를 입력하시오"))
weight=int(input("몸무게를 입력하시오"))
height_m =height_cm/100

bmi=weight/pow(height_m,2)
print("키가 {}cm, 몸무게가 {}이면, bmi는 {}입니다".format(height_cm,weight,bmi))
