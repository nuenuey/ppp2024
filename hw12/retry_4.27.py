def read_file(filename, col_name): #col_name이라는 열(column)의 데이터를 반환
    dataset=[] #데이터 저장할 것
    with open(filename) as f: #파일을 열어서 라인을 읽을 거야
        lines = f.readlines()
        header=[x.strip() for x in lines[0].split(",")] #,을 기준으로 분할해서 헤더의 정보요소로
        col_idx = header.index(col_name) #인덱스 찾기
        
        for line in lines[1:]:
            
            dataset.append(float(line.split(",")[col_idx]))
        return dataset
    
def read_file_int(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines = f.readlines()
        header=[x.strip() for x in lines[0].split(",")]
        col_idx = header.index(col_name)
        
        for line in lines[1:]:
           dataset.append(int(line.split(",")[col_idx]))
        return dataset
    

def read_date(filename):
    dataset=[]
    with open(filename) as f:
        lines = f.readlines()
    
        for line in lines[1:]:
            
            year=int(line.split(",")[0])
            month=int(line.split(",")[1])
            day=int(line.split(",")[2])
            dataset.append([year, month, day]) #리스트이름.append(추가할 요소)
        return dataset

#1 일교차가 가장 큰 날짜와 해당일자의 일교차
def maximum_temp_gap(dates, tmax, tmin):
    max_gap = 0
    max_gap_date = None

    for date, max_temp, min_temp in zip(dates, tmax, tmin):
        gap = max_temp - min_temp
        if gap > max_gap:
            max_gap = gap
            max_gap_date = date

    return max_gap_date, max_gap  #최고 일교차 날짜, 일교차값

#적산온도 구하기=> 5-9월 생육도일 (적산온도, GDD, drowing degree dat=ys)
def gdd_season(tavg_data, months):
    gdd_sum = 0
    for temp, month in zip(tavg_data, months):
        if month in [5, 6, 7, 8, 9]:
            eff_temp = temp - 5
            if eff_temp < 0:
                eff_temp = 0
            gdd_sum += eff_temp
    return gdd_sum



def main():
   
    weather_filename_22 = "hw12/weather(146)_2001-2022 (1).csv"
    tmax=read_file(filename,"tmax")
    tmin=read_file(filename,"tmin")
    date=read_file(filename,"")
    tavg = read_col(weather_filename_22, "tavg")
    months = read_col_int(weather_filename_22, "month")

    print(f"GDD는 {gdd_season(tavg,months):.1f}도일입니다.")

if __name__ == "__main__":
    main()
