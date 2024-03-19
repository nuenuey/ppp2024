#비만 정도를 표시/ 조건절

height_cm= int(input("키를 입력하시오"))
weight=int(input("몸무게를 입력하시오"))
height_m =height_cm/100

bmi=weight/(height_m*height_m)

if bmi<= 23:
     print("BMI값이 {}이고 정상입니다".format(bmi))
elif bmi <= 24.9:
        print("BMI값이 {}이고 비만 전 단계입니다".format(bmi))
elif bmi <= 29.9:
        print("BMI값이 {}이고 1단계 비만입니다".format(bmi))
elif bmi <= 34.9:
        print("BMI값이 {}이고 2단계 비만입니다".format(bmi))
else:
        print("BMI값이 {}이고 3단계 비만입니다".format(bmi))
