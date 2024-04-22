from weather_stat import read_col, read_col_int


def read_col(filename, col_name):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        col_idx = header.index(col_name)
        
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset

def read_col_int(filename, col_name):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        col_idx = header.index(col_name)
        
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(int(tokens[col_idx]))
    return dataset

    
def maximum_temp_gap(dates, tmax, tmin):
    max_gap = 0
    max_gap_date = None

    for date, max_temp, min_temp in zip(dates, tmax, tmin):
        gap = max_temp - min_temp
        if gap > max_gap:
            max_gap = gap
            max_gap_date = date

    return max_gap_date, max_gap

def filter_month(data, dates, months):
    filtered_data = [value for value, date in zip(data, dates) if date.month in months]
    return filtered_data


def gdd_season(tavg_data, months):
    gdd_sum=0

    for temp, month in zip(tavg_data,months):
        if month in [5, 6, 7, 8, 9]:
            eff_temp =temp -5
            if eff_temp < 0:
                eff_temp =0
            gdd_sum += eff_temp

    return gdd_sum

def main():
    # 예시 데이터
    # File names
    weather_filename = "hw12/weather(146)_2001-2022 (1).csv"
    weather_filename_22 = "hw12/weather(146)_2022-2022.csv"

    # Reading data
    tavg = read_col(weather_filename_22, "tavg")
    tmax= read_col(weather_filename_22,"tmax")
    tmin= read_col(weather_filename_22,"tmin")

    rainfall=read_col(weather_filename_22,"rainfall")
    months_float= read_col(weather_filename_22,"month")
    months= [int(x) for x in months_float]
    months= read_col_int(weather_filename_22, "month")
    # 최대 일교차 구하기
    max_gap_date, max_gap = maximum_temp_gap(dates, tmax, tmin)
    print(f" 최대 일교차는{max_gap_date}: {max_gap}℃")

    # 5월부터 9월까지의 생육도일(GDD) 구하기
    filtered_tavg = filter_month(tavg, dates, [5, 6, 7, 8, 9])
    total_gdd = gdd_season(filtered_tavg)
    print(f": {total_gdd}")

if __name__ == "__main__":
    main()