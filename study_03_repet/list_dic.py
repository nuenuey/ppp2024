rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

for color in rainbow:  
    print(color)       

total = 0  # 합계

for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if n % 2 == 0:  # n 이 짝수인 경우,
        total += n  # total에 n을 더함

print(total)

#실습
mart = {"우유": 2800, "계란": 300, "빵": 1200, "물": 1700}
# cart에 하나씩 담는다.
# cart = []
# cart.append(“물”)                             기존의 리스트의 끝부분에 추가하겠다
# cart.append(“물”)
#cart = ["물", "물", "계란", "빵", "빵", "빵"] # 모두 다 담았다고 가정
#total_cost = 0
#for item in cart:
#    total_cost += mart[item]
#print("총 구매금액은 {:,}원입니다.".format(total_cost))

#마켓에서 카트에 물건을 담고 그 물건을 계산하기
mart = {"우유": 2800, "계란": 300, "빵": 1200, "물": 1700}
cart=[]
cart.append("물")
cart.append("물")
cart.append("계란")
total_cost=0
for item in cart:
   total_cost+= mart[item]



#과제5
#2 삼각형 별
#3 삼각함수 표 만들기

#2
