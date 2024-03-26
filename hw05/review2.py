import math
for deg in range(0,91,15):
    rad =math.pi *deg /180
    if deg ==90:
        print(f"{deg:4d} {math.sin(rad):6.4f} {math.cos(rad):6.4f} {math.tan(rad):6.4f}")
    else:
        print(f"{deg:4d} {math.sin(rad):6.4f} {math.cos(rad):6.4f} {'N/A' :^6}")
#6. 전체 자릿수 :< 왼쪽 정렬 := :^ 가운데 정렬
