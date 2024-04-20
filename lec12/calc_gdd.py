from weather_stat import read_col, read_col_int
#from weather_stat import read_col, read_col_int

def gdd_season(tavg, months):
    total_gdd=0

    for temp, month in zip(tavg,months):
        if month in [5, 6, 7, 8, 9]:
            eff_temp =temp -5
            if eff_temp < 0:
                eff_temp =0
            total_gdd += eff_temp


    #total_gdd=sum([temp -5 if temp > 5 else 0 for temp, month
    #                in zip (tavg,months) if month in [5, 6, 7, 8, 9]  ])
    return total_gdd



def main():
    filename="lec12/weather(146)_2022-2022 (1).csv"
    tavg= read_col(filename,"tavg")
    months= read_col_int(filename,"month")

    print(f"GDD는 {gdd_season(tavg,months):.1f}도일입니다.")

    
if __name__ == "__main__":
    main()