#겨울철, 여름철 온도분포는?
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


    tmax = read_col_int(filename, "최고기온(℃)")
    dates = read_date(filename)
    months = dates[1]

    winter_temps = []
    summer_temps = []

    for i in range(len(months)):
        month = months[i]
        temp = tmax[i]

        # 겨울철
        if month in [12, 1, 2]:
            winter_temps.append((month, temp))

        # 여름철
        if month in [6, 7, 8]:
            summer_temps.append((month, temp))

    winter_months, winter_values = zip(*winter_temps)
    summer_months, summer_values = zip(*summer_temps)

    plt.figure(figsize=(12, 6))
    plt.scatter(winter_months, winter_values, color='blue', label='겨울철 온도분포')
    plt.scatter(summer_months, summer_values, color='red', label='여름철 온도분포')

    plt.xlabel('월')
    plt.ylabel(' 최고기온(℃)')
    plt.title('여름철과 겨울철의 최고기온분포')
    plt.legend()
    #plt.show()
    plt.savefig("./summer_winter_dot.png")
if __name__ == "__main__":
    main()