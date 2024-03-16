#칼로리 구하기

strawberry= int(input("딸기의 섭취 g을 입력하시오."))
Hanrabong= int(input("한라봉의 섭취 g을 입력하시오."))
banana= int(input("바나나의 섭취 g을 입력하시오."))

s_calorie=50/100*strawberry
h_calorie=34/100*Hanrabong
b_calorie=77/100*banana
total_calories =s_calorie+h_calorie+b_calorie
print("당신이 먹은 딸기의 섭취 칼로리는 {}이고, 한라봉의 섭취 칼로리는 {}이고, 바나나의 섭취 칼로리는{}입니다. 총 당신은 {}칼로리를 과일로 섭취하였습니다.".format(s_calorie,h_calorie ,b_calorie, total_calories))