def read_average_temper_y(filename): #연평균 기온 idx=4
    #return[3,5,5,7,10]
    results=[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens=line.split(',')
            tavg= float(tokens[4]) #리스트 그 자체
            results.append(tavg)
        return results


def read_over_5mm_rain(filename): #5mm 이상 강우일수 idx=9
    #return[3,5,5,7,10]
    results=[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens=line.split(',')
            rainfall= float(tokens[9])
            results.append(rainfall)
           
    over_5mm_rainfall = [rainfall for rainfall in results if rainfall >= 5]
    return over_5mm_rainfall


def read_total_rainfall(filename): #총 강우량 
    #return[3,5,5,7,10]
    results=[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens=line.split(',')
            total_rainfall= float(tokens[9])
            results.append(total_rainfall)
        return results
#총강우량의 리스트 만듦.... 리스트 값을 더해야 총강우량의 합
    
def main():

    tavg=read_average_temper_y("hw10/weather(146)_2022-2022 (1).csv") #리스트 값 그 자체
    tavg_y= (sum(tavg))/len(tavg)# 리스트 안 숫자

    rainfall=read_over_5mm_rain("hw10/weather(146)_2022-2022 (1).csv")
    # 5mm이상이 몇 개 인지
    over_5mm_rainfall=len(rainfall)
                        
    total_rainfall=read_total_rainfall("hw10/weather(146)_2022-2022 (1).csv")
    count_total_rainfall=sum(total_rainfall)

    print(f"연 평균 기온은{(tavg_y):.1f}C 입니다.")
    print(f"5mm 이상 강우일수는{(over_5mm_rainfall):.0f}일 입니다.")
    print(f"총 강우량은 {(count_total_rainfall):.1f} 입니다.")


if __name__ == "__main__":
    main()