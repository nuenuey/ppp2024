# concat 붙인다

def total_calorie(fruits_eat, fruits_cal_dic):
    # 방법 1
    # total = 0
    # for fruit_name in fruits_eat:
    #     total += fruits_eat[fruit_name] * fruits_cal_dic[fruit_name] / 100
    # return total

    # 방법 2
    # total = 0
    # for fruit_name, fruit_gram in fruits_eat.items():
    #     total += fruit_gram * fruits_cal_dic[fruit_name] / 100
    # return total

    # 방법 3
    return sum([gram*fruits_cal_dic[name]/100
                for name, gram in fruits_eat.items()])

def read_cal_db (filename):
    database ={}
    with open(filename, encoding="utf-8-sig") as f:
        lines =f.readlines()

        for line in lines[1:]: #두 번째 줄부터
            tokens=line.split(",") #,을 기준으로 자른다

            fruit_name= tokens[0] 
            fruit_cal= int(tokens[1])
            database[fruit_name] = fruit_cal
        
    return database



def main():
    # fruits_calorie_dic = {"귤": 39, "딸기": 34, "바나나": 77}
    
    fruits_calorie_dic = read_cal_db("lec10/calorie_db.csv")
    fruits_mon = {"딸기": 300, "귤": 150}
    print(total_calorie(fruits_mon, fruits_calorie_dic))
    
    fruits_wed = {"딸기": 200, "바나나": 300}
    print(total_calorie(fruits_wed, fruits_calorie_dic))




if __name__ == "__main__":
    main()