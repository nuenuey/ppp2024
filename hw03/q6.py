#두 지점 사이 거리 구하기

x1= int(input("x1의 좌표를 입력하시오"))
y1= int(input("y1의 죄표를 입력하시오"))
x2= int(input("x2의 좌표를 입력하시오"))
y2= int(input("y2의 좌표를 입력하시오"))
one_point=("({},{})".format(x1,y1))
other_point=("({},{})".format(x2,y2))
calculator= ((x2-x1)**2+(y2-y1)**2)**0.5

last=print("한 좌표가{}이고, 다른 좌표가{}일때, 두 지점 사이의 거리는 {}입니다." .format(one_point,other_point,calculator))