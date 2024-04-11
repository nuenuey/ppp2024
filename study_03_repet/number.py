#1-4까지 출력하는 프로그램

number = 0      # 수를 세기 위해 변수가 필요하다

number += 1     # 수를 1 증가시킨다
print(number)   # 수를 출력한다
number += 1
print(number)
number += 1
print(number)
number += 1
print(number) 

for i in range(4):
    print(i+1)

#실습 1-100까지 합계
total=0
for i in range(100):
    total=total+ (i+1)

print(total)
print(f"250까지의짝수 합은 {total:,}입니다.") #5050 => 5,050
#구구단 2단 출력
dan=2
for i in range(9):
    print(f"{dan}*{i+1}=",dan*(i+1))


#1-250까지 짝수의 합
total2=0
for i in range(250):
    if (i+1)%2==0:
        total2=total2+ (i+1)
print(total2)
print(f"250까지의짝수 합은 {total2:,}입니다.")
#합계를 구하라할땐, total 을 많이씀
