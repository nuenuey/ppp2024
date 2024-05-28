# #내 생일날 기온은 어땠나? 몇살 생일때가 춥고, 더웠나? 내가 태어나기 전에도 날씨가 동일한 패턴이었던가?
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
    #한글로 쓰고 싶을 때

    #달, 월이 특정값일떄
    dates = read_date(filename)
    years = dates[0]
    months = dates[1]
    days = dates[2]


    avg_temps = read_col_int(filename, "평균기온(℃)")
    birth_years = []
    birth_avg_temps = []
    for i in range(len(years)):
        if months[i] == 2 and days[i] == 6:
            birth_years.append(years[i])
            birth_avg_temps.append(avg_temps[i])


    plt.plot(birth_years, birth_avg_temps,color="r", label="기온 2/6")
    plt.title("내 생일 평균기온 변화")
    plt.xlabel("연도")  # y축이름
    plt.ylabel("기온(℃)") #y축이름
    plt.legend()
    #plt.show()
    plt.savefig("./birth_temp_line.png")
if __name__ == "__main__":
    main()