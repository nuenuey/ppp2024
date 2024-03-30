#총 칼로리 계산하기

def  total_calorie(fruits, fruits_calorie_dic):
    
    #100g당 과일의 칼로리 dic
    fruits_calories_dic={
    "한라봉":50, "딸기":34, "바나나":77
    }
    #섭취한 칼로리 계산하기
    total_calories = 0
    for fruit, amount in fruits.items():
        if fruit in fruits_calories_dic:
            total_calories += fruits_calories_dic[fruit] * amount /100
    return total_calories


def main():
    

    fruits = {"딸기": 300, "한라봉": 150}

    #100g당 과일의 칼로리 dic
    fruits_calories_dic={
    "한라봉":50, "딸기":34, "바나나":77
    }
    total_calories = total_calorie(fruits, fruits_calories_dic)

    print(f"섭취한 딸기 300g, 한라봉 150g의 칼로리는 {total_calories:.2f} kcal입니다.")


if __name__ == "__main__":
    main()


