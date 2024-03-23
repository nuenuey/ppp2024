# x, y를 입력받아서, 어느 사분면인지 출력

x1= int(input("x1의 좌표를 입력하시오"))
y1= int(input("y1의 죄표를 입력하시오"))

if x1>0:
    if y1>0:
        print("({},{})은 1사분면에 있습니다".format(x1,y1)) 
    else:
        print("({},{})은 4사분면에 있습니다".format(x1,y1))
else:
    if y1>0:
        print("({},{})은 2사분면에 있습니다".format(x1,y1)) 
    else:
        print("({},{})은 3사분면에 있습니다".format(x1,y1))

#교수님
#if x==0 and y==0:
#        print("({},{})는 중심입니다".format(x,y))
#중심, 1,2,3,4분면, y축위, x축위