from weather_q78 import read_col, read_col_int

def main():
    filename="lec10/weather(146)_2022-2022.csv"
    tmax=read_col(filename, "tmax")
    tmin=read_col(filename, "tmin")
    years=read_col_int(filename, "year")
    months=read_col_int(filename, "month")
    days=read_col_int(filename, "day")

    # 방법1
    temp_diff=[]
    for tx, tn in zip(tmax, tmin):
        temp_diff.append(tx-tn)
        
    #temp_diff=tmax-tmin

    # 방법2
    #for i in range(len(tmax)):
    #    temp_diff.append(tmax[i]-tmin[i])
    
    # 방법3
    #temp_diff=[tx-tn for tx, tn in zip(tmax, tmin)]

    max_idx=0
    max_diff_temp=0
    i=0
    for td in temp_diff:
        if max_diff_temp<td:
            max_diff_temp=td
            max_idx=i
        i+=1

    print(f"일교차가 가장 큰 날짜는 {years[max_idx]}/{months[max_idx]}/{days[max_idx]}, 최대일교차는 {max(temp_diff):.1f}℃ 입니다.")

if __name__=="__main__":
    main()