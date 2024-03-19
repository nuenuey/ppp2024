#칼로리 계산 프로그램을 사전형

#섭취한 과일양
eat_strawberry= int(input("딸기의 섭취 g을 입력하시오."))
eat_Hanrabong= int(input("한라봉의 섭취 g을 입력하시오."))
eat_banana= int(input("바나나의 섭취 g을 입력하시오."))
#100g당 과일의 칼로리 dic
calories={
    "딸기":0.34, "한라봉":0.50, "바나나":0.77
    }
#섭취한 칼로리 계산하기
total_calories = calories["딸기"]*eat_strawberry + calories["한라봉"]*eat_Hanrabong+ calories["바나나"]*eat_banana

print("총 섭취한 과일의 칼로리는{}g입니다".format(total_calories))
