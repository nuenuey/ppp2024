print("각ㅣradㅣsinㅣcosㅣtan")

sin =0
cos =0
tan =0
degree=0
radian=0


for i in range(10):
    degree=degree +1
    radian=radian+1
    sin=sin+1
    cos=cos+1
    tan=tan+1

    import math
    A_radian=math.radians(radian)
    A_sin=math.sin((sin))
    A_cos=math.cos((cos))
    A_tan=math.tan((tan))



    print(f"{degree:,}ºㅣ{A_radian:.4f}ㅣ{A_sin:,.4f}ㅣ{A_sin:.4f}ㅣ{A_tan:.4f}" )
   

