def total_calorie(fruits_eat, fruits_calorie_dic):
    total=0
    for fruits_name in fruits_eat:
       # print(fruits_name)
        total+= fruits_eat[fruits_name]* fruits_calorie_dic[fruits_name] /100

    return total

#방법2
#   total=0
#  for fruit_name, fruit_gram in fruits_eat.items():
#       total += fruits_eat * fruits_calorie_dic[fruits_name]/100
#       return total

#방법 3
#   return sum ([gram*fruits_calorie_dic[name]/100
#                for name,gram in fruits_eat.item()])
def main():
    fruits_calorie_dic = {"한라봉": 50, "딸기": 34, "바나나": 77}


    fruits_mon={"딸기": 300, "한라봉": 150}
    print(total_calorie(fruits_mon, fruits_calorie_dic))

    fruits_wed={"딸기": 200, "바나나": 300}
    print(total_calorie(fruits_wed, fruits_calorie_dic))




if __name__ == "__main__":
    main()