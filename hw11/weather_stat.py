def read_col(filename, col_name): #col_name= 읽어올 열의 이름
    dataset=[]
    with open(filename) as f:
        lines = f.readlines()
        header=[x.strip() for x in lines[0].split(",")] #헤더, 열의 이름을 리스트로 저장
        col_idx= header.index(col_name) #헤더이름과 인덱스의 매치
        #print(header)
        for line in lines[1:]:
            tokens=line.split(",")
            dataset.append(float(tokens[col_idx]))
        return dataset

def read_col_int(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines = f.readlines()
        header=[x.strip() for x in lines[0].split(",")]
        col_idx = header.index(col_name)
        #print(header)
        for line in lines[1:]:
            tokens=line.split(",")
            dataset.append(int(tokens[col_idx]))
        return dataset  
    
#def count_rainday(rainfall):
   # rain_day=0
   # for rain in rainfall:
   #     if rain>=5:
   #         rain_day += 1
    return sum([1 if x >= 5 else 0 for x in rainfall]) # 조건 맞으면 앞, 아니면 뒤에

def longest_rainday(rainfall): # 비가 오면 1, 안오면 0 비가연속되어 오면 1234, 4일 (마지막 숫자 기억)
     rain_event= []
     prev_rain_count=0
     
     for rain in rainfall:
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain_count)
            prev_rain_count=0
        else:
            prev_rain_count+=1 #맨마지막 값을 저장해야해, 맨 마지막값은 비가 안오면 저장
     return max(rain_event)


def max_rainfall_event(rainfall): # 비가 오면 1, 안오면 0 비가연속되어 오면 1234, 4일 (마지막 숫자 기억)
     rain_event= []
     prev_rain=0
     prev_rain_count =0

     for rain in rainfall:
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain)
            prev_rain_count=0
            prev_rain=0
        else:
            prev_rain_count+=1 #맨마지막 값을 저장해야해, 맨 마지막값은 비가 안오면 저장
            prev_rain+=rain
     return max(rain_event)

  
def  top_rank(values, limit):
    # return sorted(values, reverse=True)[-limit:]
    return sorted(values)[-limit:][::-1]

def sumifs(rainfall, months, conditions):
    total=0
    #for i in range (len(rainfall)):
    #    rain= rainfall[i]
    #    month= months[i]
    #    if month in conditions:
    #        total+= rain
    for rain, month in zip (rainfall, months):
        if month in conditions:
            total += rain
    return total
        


def read_col_year(weather_filename, col_name, year): #매계변수 3개
    dataset=[] #연도 저장할 거임
    with open(weather_filename) as f:
        lines = f.readlines()
        header=[x.strip() for x in lines[0].split(",")]
        col_idx= header.index(col_name)
        for line in lines[1:]:
            tokens=line.split(",")
            y= int(tokens[0]) #연도
            if y == year:
                dataset.append(float(tokens[col_idx]))
        return dataset
    
def get_data_ifs(values, conditions,criteria):
    #dataset=[]
    #for rain, year in zip(values, conditions):
    #    if year == criteria:
    #        dataset.append(rain)
    #return dataset
    return [rain for rain, year in zip (values, conditions) if year== criteria]
    #year가 criteria와 같은지 확인하고, 조건을 만족하는 rain 값을 리스트에 저장
    #조건을 만족하는 rain 값들로 구성된 리스트를 반환함

def main():
    weather_filename = "hw11/weather(146)_2001-2022.csv"
    weather_filename_22="hw11/weather(146)_2022-2022 (1).csv"
    
    tmax= read_col(weather_filename_22,"tmax")
    rainfall=read_col(weather_filename_22,"rainfall")
    months_float= read_col(weather_filename_22,"month")
    months= [int(x) for x in months_float]
    months= read_col_int(weather_filename_22, "month")
    

    


#4번 최장연속강우일수
    print(f"최장연속 강우일수는 {longest_rainday(rainfall)}일 입니다.")
#5번 강우이벤트 중 최대 강수량은
    print(f"최대 강우량은 {max_rainfall_event(rainfall):.1f}mm입니다.")
#6번 가장 더운날 top 3(tmax의 최댓값 3개)
    print(f"가장 더운 날 top3는 {top_rank(tmax, 3)}mm입니다.") 
#7번 6, 7, 8월 총강수량
    print(f"여름철(6월-8월) 총 강수량은 {sumifs(rainfall, months,[6,7,8]):.1f}mm 입니다.")
#8번 2021, 2022년 강수량
    rainfall_all = read_col(weather_filename, "rainfall") 
    year_all = read_col_int(weather_filename,"year")  
    rainfall_2021 = get_data_ifs(rainfall_all, year_all, 2021) 
    #rainfall_2021 = read_col_year(weather_filename, "rainfall", 2021)
    print(f"총강수량은 {sum(rainfall_2021):.1f}mm입니다.")



if __name__ == "__main__":
    main()