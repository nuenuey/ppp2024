import sys
if "./" not in sys.path:
    sys.path.append("./")


import requests
from lec14 import hw_submission
#from hw11.weather_stat import read_col, read_col_int #헤더와 인덱스 매치


def download(filename,URL):
    with open(filename, "w", encoding="utf-8") as f:
        res = requests.get(URL) #포스트에 url있고 자료널기
        res.encoding="cp949"
        f.write(res.text.replace("\r",""))

def read_col(filename, col_name): #col_name= 읽어올 열의 이름
    dataset=[]
    with open(filename) as f:
        lines = f.readlines()
        header=[x.strip() for x in lines[7].split(",")] #헤더, 열의 이름을 리스트로 저장
        col_idx= header.index(col_name) #헤더이름과 인덱스의 매치
        #print(header)
        for line in lines[8:]:
            cutdata = tokens=line.split(",")
            
            if cutdata != '':  # 빈칸이 아닌 경우에만 추가
                dataset.append(float(tokens[col_idx]))
        return dataset

def read_col_int(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines = f.readlines()
        header=[x.strip() for x in lines[7].split(",")]
        col_idx = header.index(col_name)
        #print(header)
        for line in lines[8:]:
            cutdata = tokens=line.split(",")
            
            if cutdata != '':  # 빈칸이 아닌 경우에만 추가
                dataset.append(int(tokens[col_idx]))
        return dataset  




#1 일교차가 가장 큰 날짜와 해당일자의 일교차
def maximum_temp_gap(tmax, tmin,dates):
    tdiff_max  = 0
    tdiff_max_date = None

    for date, max_temp, min_temp in zip(dates, tmax, tmin):#날짜, 최고온도, 최저온도=> 일교차 찾기
        gap = max_temp - min_temp
        if gap > tdiff_max:
            tdiff_max = gap
            tdiff_max_date = date

    return tdiff_max_date, tdiff_max  #최고 일교차 날짜, 일교차 값

def read_date(filename):
    dataset=[]
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:  
            
            year=int(line.split(",")[0])
            month=int(line.split(",")[1])
            day=int(line.split(",")[2])
            dataset.append([year, month, day]) #리스트이름.append(추가할요소)
        return dataset
    


def main():
    URL="https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    filename="hw14/jeonju_all.csv"
    download(filename, URL)

    # 전주에서 최고기온, tmax
    # 그 날짜 tmax_date
    # 최대 일교차 tdiff_max----0
    # 최대 일교차날  tdiff_max_date-----0

    #tmax,tmax_date =????
    #tdiff_max, tdiff_max_date = ?????
    
    
    #tavg = read_col(filename, "평균기온(℃)")
    tmin = read_col(filename, "최저기온(℃)") 
    tmax = read_col(filename, "최고기온(℃)") 
    dates = read_date(filename)
    
    #최고기온 구하는 방법=> 최고기온 최저기온의 차이 계산해서
    #차이가 가장 큰 값이 최고기온 날짜
    temp_diff = [tx - tn for tx, tn in zip(tmax, tmin)]
    max_value = max(temp_diff)
    #그 날짜 인덱스 찾기
    max_idx = temp_diff.index(max_value)
    tmax_date = dates[max_idx]
    

    # 최대 일교차 날짜 # 일교차 값
    tdiff_max_date, tdiff_max  = maximum_temp_gap(dates, tmax, tmin)
    print(f"최대 일교차 값은{tdiff_max:.1f}C ---- 최대 일교차 날짜는 {tdiff_max_date}")



    print(f"최대기온의 값은 {max(tmax)}C ---- 최대기온의 날짜는 {tmax_date}이고")
    # 최대 기온 날짜 # 최고기온 값
    
    
    #tmax,tmax_date = 38,"2021-08-12"
    #tdiff_max, tdiff_max_date = 28.5, "1989-08-12"

    hw_submission.submit("홍길동", tmax, tmax_date, tdiff_max, tdiff_max_date)



if __name__ == "__main__":
    main()