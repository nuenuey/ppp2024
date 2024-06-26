import sys

if "./" not in sys.path:
    sys.path.append("./")

from hw11.weather_stat import read_col, read_col_int
#from weather_stat import read_col, read_col_int

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
   
    weather_filename_22 = "hw12/weather(146)_2022-2022.csv"


    tavg = read_col(weather_filename_22, "tavg")
    months = read_col_int(weather_filename_22, "month")

    print(f"GDD는 {gdd_season(tavg,months):.1f}도일입니다.")

if __name__ == "__main__":
    main()