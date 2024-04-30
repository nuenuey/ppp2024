import sys

if "./" not in sys.path:
    sys.path.append("./")

from hw11.weather_stat import read_col, read_col_int
from lec12.find_max_temper import read_file, read_file_int



#1 일교차가 가장 큰 날짜와 해당일자의 일교차
def maximum_temp_gap(dates, tmax, tmin):
    max_gap = 0
    max_gap_date = None

    for date, max_temp, min_temp in zip(dates, tmax, tmin):#날짜, 최고온도, 최저온도=> 일교차 찾기
        gap = max_temp - min_temp
        if gap > max_gap:
            max_gap = gap
            max_gap_date = date

    return max_gap_date, max_gap  #최고 일교차 날짜, 일교차 값

#적산온도 구하기=> 5-9월 생육도일 (적산온도, GDD, drowing degree dat=ys)
def gdd_season(tavg_data, months):
    gdd_sum = 0
    for temp, month in zip(tavg_data, months): ##zip(리스트,리스트) 리스트에서 인덱스요소를 가져와 temp와 month라는 변수에 할당
        if month in [5, 6, 7, 8, 9]: #gdd계산 
            eff_temp = temp - 5
            if eff_temp < 0: #음수일때->0
                eff_temp = 0
            gdd_sum += eff_temp
    return gdd_sum



def main():
   
    filename = "hw12/weather(146)_2001-2022 (1).csv"
    years= read_date(filename)
    tavg = read_col(filename, "tavg")
    tmin = read_col(filename, "tmin")
    months = read_col_int(filename, "month")
    dates = read_date(filename)

#여기 솔직히 이해 X
    # 최대 일교차 날짜 # 일교차 값
    max_gap_date, max_gap = maximum_temp_gap(dates, tavg, tmin)

    
   # 적산온도
    gdd = gdd_season(tavg, months)


   # print(f"최대 일교차 날짜는 {max_gap_date[0]:04d}년 {max_gap_date[1]:02d}월 {max_gap_date[2]:02d}일---일교차 값{max_gap:.1f}C")
    print(f"{years}년--- 적산온도{gdd:.1f}C")  

if __name__ == "__main__":
    main()
