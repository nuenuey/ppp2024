def read_col(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines = f.readlines()
        header=[x.strip() for x in lines[0].split(",")]
        col_idx= header.index(col_name)
        
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
    
def count_rainday(rainfall):
   rain_day=0
   for rain in rainfall:
       if rain>=5:
           rain_day += 1
    return sum([1 if x >= 5 else 0 for x in rainfall]) # 조건 맞으면 앞, 아니면 뒤에

def longest_rainday(rainfall): 
     rain_event= []
     prev_rain_count=0
     
     for rain in rainfall:
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain_count)
            prev_rain_count=0
        else:
            prev_rain_count+=1 
     return max(rain_event)


def max_rainfall_event(rainfall): 
     prev_rain=0
     prev_rain_count =0

     for rain in rainfall:
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain)
            prev_rain_count=0
            prev_rain=0
        else:
            prev_rain_count+=1 
            prev_rain+=rain
     return max(rain_event)

  
def  top_rank(values, limit):
    
    return sorted(values)[-limit:][::-1]

def sumifs(rainfall, months, conditions):
    total=0
    
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
    return [rain for rain, year in zip (values, conditions) if year== criteria]
   
def main():
    weather_filename = "hw12/weather(146)_2001-2022 (1).csv"
    weather_filename_22="hw12/weather(146)_2022-2022.csv"
    
    tmax= read_col(weather_filename_22,"tmax")
    rainfall=read_col(weather_filename_22,"rainfall")
    months_float= read_col(weather_filename_22,"month")
    months= [int(x) for x in months_float]
    months= read_col_int(weather_filename_22, "month")
    rainfall_all = read_col(weather_filename, "rainfall") 
    year_all = read_col_int(weather_filename,"year")  
    #21
    rainfall_2021 = get_data_ifs(rainfall_all, year_all, 2021) 
    #rainfall_2021 = read_col_year(weather_filename, "rainfall", 2021)
    print(f"2021년 총강수량은 {sum(rainfall_2021):.1f}mm입니다.")
    #22
    rainfall_2022 = get_data_ifs(rainfall_all, year_all, 2022) 
    #rainfall_2022 = read_col_year(weather_filename, "rainfall", 2022)
    print(f"2022년 총강수량은 {sum(rainfall_2022):.1f}mm입니다.")

if __name__ == "__main__":
    main()