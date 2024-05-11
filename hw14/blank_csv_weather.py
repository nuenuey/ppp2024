import sys
if "./" not in sys.path:
    sys.path.append("./")

import requests
from lec14 import hw_submission
#from hw11.weather_stat import read_col, read_col_int #헤더와 인덱스 매치
# from hw12_maximum_temp_gap.retry import read_date


def download(filename,URL):
   with open(filename, 'w', encoding='UTF-8') as f:
        res = requests.get(URL) #포스트에 url있고 자료널기
        # res.encoding='cp949'
        f.write(res.text.replace("\r",""))
        # res.encoding = res.apparent_encoding
        # f.write(res.content.decode(res.apparent_encoding).replace("\r", ""))

def read_date(filename):
    dataset=[]
    with open(filename, encoding='UTF-8') as f:
        lines = f.readlines()
        #print(lines)
        for line in lines[8:]:
            token = line.split(',')
            token = token[0].replace("\t", "")
            # token = token[4].replace("\n", "")
            #print(token)
            year=int(token.split("-")[0])
            month=int(token.split("-")[1])
            day=int(token.split("-")[2])
            dataset.append([year, month, day]) #리스트이름.append(추가할 요소)
            #print(dataset) # [1918, 6, 29], [1918, 6, 30]
        return dataset #리스트로 저장

def read_col(filename, col_name): #col_name= 읽어올 열의 이름
    dataset=[]
    with open(filename, encoding='UTF-8') as f:
        lines = f.readlines()
        header=[x.strip() for x in lines[7].split(",")] #헤더, 열의 이름을 리스트로 저장
        col_idx= header.index(col_name) #헤더이름과 인덱스의 매치
        #print(header)
        for line in lines[8:]:
            tokens = line.split(",")
            #print(tokens) #['\t2024-01-27', '146', '2.2', '-0.7', '6.5\n']
            tokens[4] = tokens[4].replace("\n", "")
            #print(tokens)# ['\t2024-04-22', '146', '17.7', '15', '21.8']
            if tokens[col_idx] != '':  # 빈칸이 아닌 경우에만 추가
                dataset.append(float(tokens[col_idx]))
            else:
                dataset.append(-999)
        # print(dataset)
        return dataset

def read_col_int(filename, col_name):
    dataset=[]
    with open(filename, encoding='UTF-8') as f:
        lines = f.readlines()
        header=[x.strip() for x in lines[7].split(",")]
        col_idx = header.index(col_name)
        #print(header)
        for line in lines[8:]: #인덱스 8번부터 세로로 끝까지 줄 읽기
            cutdata = tokens=line.split(",")
            #print(cutdata) #['\t2024-03-11', '146', '7.4', '1.6', '12.8']
            if cutdata != '':  # 빈칸이 아닌 경우에만 추가
                dataset.append(int(tokens[col_idx]))
        return dataset  

def main():
    URL="http://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    filename="./jeonju_all.csv"
    # download(filename, URL)

    #tavg = read_col(filename, "평균기온(℃)")
    tmin = read_col(filename, "최저기온(℃)") 
    tmax = read_col(filename, "최고기온(℃)") 
    dates = read_date(filename)


    ## 최대 일교차
    #최고기온 구하는 방법=> 최고기온 최저기온의 차이 계산해서
    #차이가 가장 큰 값이 최고기온 날짜
    temp_diff = [tx - tn for tx, tn in zip(tmax, tmin)] #1. 최고기온 최저기온의 차이
    temp_diff_p = [tx - tn for tx, tn in zip(tmax, tmin) if tx != -999 and tn != -999]
    diff_max_value = max(temp_diff_p) # 일교차중 최고차이
    #그 날짜 인덱스 찾기 (리스트.index(이름))
    diff_max_idx = temp_diff.index(diff_max_value)
    temp_diff_max_date = dates[diff_max_idx]

    ## 최고 기온
    # temp_diff = [tx for tx in tmax if tx != -999 ]
    temp_max = []
    for tx in tmax:
        if tx != -999:
            temp_max.append(tx)

    max_temp_value = max(temp_max)
    # 그 날짜 인덱스 찾기
    max_idx = tmax.index(max_temp_value)
    max_date = dates[max_idx]


    # 최대 일교차 날짜 # 일교차 값
    print(f"최대 일교차 값은{diff_max_value:.1f}C ---- 최대 일교차 날짜는 {temp_diff_max_date}")
    print(f"최대기온의 값은 {max_temp_value}C ---- 최대기온의 날짜는 {max_date}이고")

    hw_submission.submit("신예은",max_temp_value , max_date, diff_max_value, temp_diff_max_date)



if __name__ == "__main__":
    main()