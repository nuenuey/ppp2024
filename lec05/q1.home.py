
#실습 
#1-10출력
#for i in range(10):
#    print(i+1)   1,2,3,4,5,6,7,8,9,10
#1+10
total=0
for i in range(10):
    total=total+ i+1
print(f"1부터 10까지의 합은 {total:,}입니다.")    

total1=0
for i in range(100):
    total1 = total1 + (i+1)
print(f"1-100까지의 합은 {total1:,}입니다")

#구구단 2단을 출력하시오
dan=2
for i in range(9):
    total1 = total1 + (i+1)
print("{}*{}={}입니다" .format(i+1,dan,(i+1)*dan))
      

