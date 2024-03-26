#2. 숫자를 입력받아, 함수 gugudan(dan)만들기
def gugudan(dan):
    
    for i in range(9):
          print("{}*{}={}" .format(i+1,dan, (i+1) * dan))

dan=int(input("구구단 몇 단을 출력할까요?"))          
print(input("{} 단을 출력하겠습니다".format(dan)))

gugudan(dan)

