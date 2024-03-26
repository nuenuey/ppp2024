#총 칼로리 계산, 반복문, 사전사용

#과일종류
eat_fruits =["딸기", "한라봉", "바나나"]


#섭취한 과일양
eat_amounts = {}
for fruit in eat_fruits:
    eat_amounts[fruit] = int(input(f"{fruit}의 섭취 g을 입력하시오: "))


#100g당 과일의 칼로리 dic
calories_dic={
    "딸기":0.34, "한라봉":0.50, "바나나":0.77
    }



#섭취한 칼로리 계산하기
total_calories = 0
for fruit, amount in eat_amounts.items():
    if fruit in calories_dic:
        total_calories += calories_dic[fruit] * amount


print(f"총 섭취한 과일의 칼로리는{total_calories}g입니다")
