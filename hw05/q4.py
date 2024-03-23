#4. 삼각함수 표를 만드시오.






print("각ㅣradㅣsinㅣcosㅣtan")
degree =0
radian= 0
sin =0
cos =0
tan =0

import math
pi=math.pi
A_radian= radian*180%pi

for i in range(11):
    print(f"{degree:,}ºㅣ{A_radian:.4f}ㅣ{sin:,.4f}ㅣ{cos:.4f}ㅣ{tan:.4f}" )
    degree=degree + 1 
    radian= radian+ 1
   
