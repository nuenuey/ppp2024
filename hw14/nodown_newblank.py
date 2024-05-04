import sys
if "./" not in sys.path:
    sys.path.append("./")


from lec14 import hw_submission

def read_col(filename, col_name):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[7].split(",")] # 헤더, (쉼표로 분리해) 열의 이름을 리스트로 저장
        col_idx = header.index(col_name) # 헤더 이름과 인덱스의 매칭
        for line in lines[8:]:
            cutdata = tokens = line.split(",") #각 줄을 토큰으로 분리,
            if cutdata != '':  # 빈칸이 아닌 경우에만 
                dataset.append(float(tokens[col_idx]))#추가
        return dataset

def read_col_int(filename, col_name):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[7].split(",")]
        col_idx = header.index(col_name)
        for line in lines[8:]:
            cutdata = tokens = line.split(",")
            if cutdata != '':  # 빈칸이 아닌 경우에만 
                dataset.append(int(tokens[col_idx])) #추가
        return dataset  
#여기까지가 각 열 숫자를 리스트로 만들기  

"""중간중간, 최대온도, 최저온도 등 값이 비어있는...빈 값처리해야함 """
def maximum_temp_gap(tmax, tmin, dates):
    tdiff_max = 0 #최대 온도차가 처음엔 0이니
    tdiff_max_date = None #최대 온도차 날짜가 첨엔 없으니 none
     
    
    for date, max_temp, min_temp in zip(dates, tmax, tmin): # 날짜, 최고온도, 최저온도=> 일교차 찾기
       # """여기------- 최고온도와 최저온도가 둘다있는 경우"""
            if max_temp and min_temp is not None:
                gap = max_temp - min_temp
                if gap > tdiff_max:
                    tdiff_max = gap
                    tdiff_max_date = date
    return tdiff_max_date, tdiff_max  # 최고 일교차 날짜, 일교차 값

def read_date(filename):
    dataset=[]
    with open(filename, encoding='cp949') as f:
        lines = f.readlines()
        for line in lines[1:]:  
            
            year=int(line.split(",")[0])
            month=int(line.split(",")[1])
            day=int(line.split(",")[2])
            dataset.append([year, month, day]) #리스트이름.append(추가할요소)
        return dataset

def main():
    filename = "hw14/jeonju_all.csv"

    tmin = read_col(filename, "최저기온(℃)") 
    tmax = read_col(filename, "최고기온(℃)") 
    dates = read_date(filename)
    
    temp_diff = [tx - tn for tx, tn in zip(tmax, tmin)]
    max_value = max(temp_diff)
    max_idx = temp_diff.index(max_value)
    tmax_date = dates[max_idx]
    
    tdiff_max_date, tdiff_max  = maximum_temp_gap(dates, tmax, tmin)
    print(f"최대 일교차 값은 {tdiff_max:.1f}C ---- 최대 일교차 날짜는 {tdiff_max_date}")

    print(f"최대기온의 값은 {max(tmax)}C ---- 최대기온의 날짜는 {tmax_date}이고")

    hw_submission.submit("신예은", tmax, tmax_date, tdiff_max, tdiff_max_date)

if __name__ == "__main__":
    main()