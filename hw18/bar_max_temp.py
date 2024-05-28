import requests
import matplotlib.pyplot as plt
import numpy as np
def read_date(filename):
    years = []
    months = []
    days = []
    with open(filename, 'r', encoding='UTF8') as f:
        for _ in range(8):
            next(f)

        for line in f:
            token = line.strip()

            if token:  # token이 비어 있지 않은지 확인
                parts = token.split("-")

                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2].split(",")[0])
                years.append(year)
                months.append(month)
                days.append(day)

        dataset = [years, months, days]
        return dataset

def read_col(filename, col_name):  # col_name= 읽어올 열의 이름
    dataset = []
    with open(filename, encoding='UTF8') as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[7].split(",")]  # 헤더, 열의 이름을 리스트로 저장

        col_idx = header.index(col_name)  #헤더이름과 인덱스의 매치
        #print(header) #['날짜', '지점', '평균기온(℃)', '최저기온(℃)', '최고기온(℃)']
        for line in lines[8:]:
            tokens = line.split(",")

            if len(tokens) == 5 and tokens[0]:  # 첫 번째 토큰이 비어 있지 않은 경우에만 처리
                tokens[col_idx] = tokens[col_idx].replace("\n", "")
                dataset.append(tokens[col_idx].strip())
        #print(dataset)
        return dataset


def read_col_int(filename, col_name):
    dataset = []
    with open(filename, encoding='UTF8') as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[7].split(",")]
        col_idx = header.index(col_name)
        #print(header)
        for line in lines[8:]:  #인덱스 8번부터 세로로 끝까지 줄 읽기
            tokens = line.split(",")
            if len(tokens) == 5 and tokens[0]:  # 첫 번째 토큰이 비어 있지 않은 경우에만 처리
                value = tokens[col_idx].strip()
                dataset.append(float(value) if value else np.nan)
            else:
                pass
        return dataset


def main():
    filename = "./ta_20240528110213.csv"
    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    # 한글로 쓰고 싶을 때


    tmax = read_col(filename, "최고기온(℃)")
    dates = read_date(filename)

    max_temp_by_year = {}
    for year, temp in zip(dates[0], tmax):
        if year not in max_temp_by_year:
            max_temp_by_year[year] = temp
        else:
            if temp != -999 and temp > max_temp_by_year[year]:
                max_temp_by_year[year] = temp

        # 최고 기온/ 연도별 / 막대 그래프 => 어느 연도가 가장 높은 최고기온
    fig, ax = plt.subplots(figsize=(15, 6))  # 사이즈 조절
    year = [str(x + 1980) for x in range(44)]  # 20개
    max_temps = list(max_temp_by_year.values())
    ax.bar(year, max_temps, color="b")  # (x축, y축) 이렃게 해라
    ax.set_ylabel("연도별 최고기온(℃)")
    plt.savefig("./max_temp_by_year_bar.png")
    #plt.show()

# 최고 기온
    temp_diff = [tx for tx in tmax if tx != -999 ]

    temp_max = []
    for tx in tmax:
        if tx != -999:
            temp_max.append(tx)

    max_temp_value = max(temp_max)
    # 그 날짜 인덱스 찾기
    max_idx: int = tmax.index(max_temp_value)
## 같은 연도중 최고 기온 찾기


#최고기온
#44년중 최고기온 날짜 => 1980년3월13일
    #print("최고기온 인덱스의 연도:", dates[0][max_idx])
    #print("최고기온 인덱스의 달:", dates[1][max_idx])
    #print("최고기온 인덱스의 일:", dates[2][max_idx])
    print(f"44년 중 최고기온 인덱스의 날짜는 {dates[0][max_idx]}년 {dates[1][max_idx]}월 {dates[2][max_idx]}일" )
    #max_date = dates[max_idx]
#44년중 최고기온 값
    print(f"44년 중 최대기온의 값은 {max_temp_value}C ")

if __name__ == "__main__":
    main()




