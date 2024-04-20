from weather_stat import read_col, read_col_int

def read_file(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines = f.readlines()
        header=[x.strip() for x in lines[0].split(",")]
        col_idx = header.index(col_name)
        
        for line in lines[1:]:
            
            dataset.append(float(line.split(",")[col_idx]))
        return dataset
    
def read_file_int(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines = f.readlines()
        header=[x.strip() for x in lines[0].split(",")]
        col_idx = header.index(col_name)
        
        for line in lines[1:]:
           dataset.append(int(line.split(",")[col_idx]))
        return dataset
    
def read_date(filename):
    dataset=[]
    with open(filename) as f:
        lines = f.readlines()
    
        for line in lines[1:]:
            
            year=int(line.split(",")[0])
            month=int(line.split(",")[1])
            day=int(line.split(",")[2])
            dataset.append([year, month, day])
        return dataset

    


    
def main():

    filename="lec12/weather(146)_2022-2022 (1).csv"
    tmax=read_file(filename,"tmax")
    tmin=read_file(filename,"tmin")
    years= read_file_int(filename,"year")
    months= read_file_int(filename,"month")
    days= read_file_int(filename,"day")
    dates=read_date(filename)
    #temp_diff= tmax-tmin #리스트에서 리스트 빼지 못함=>
    
    
    #1
    #temp_diff=[]
    #for tx in zip(tmax,tmin):
    #    temp_diff.append(tx-tn)
    temp_diff=[tx - tn for tx, tn in zip(tmax,tmin)]

    # #2
    # temp_diff=[]
    # for i in range(len(tmax)):
    #     temp_diff.append(tmax[i] -tmin[i])

    # #3
    #     max_idx=0
    #     max_diff_temp= 0
    #     i=0
    #     for td in temp_diff:
    #         if max_diff_temp<td:
    #             max_diff_temp=td
    #             max_idx = i
    #         i +=1
       

    # max_idx=0
    # max_diff_temp= 0
    # for i, td in enumerate(temp_diff):
    #     if max_diff_temp<td:
    #         max_diff_temp=td
    #         max_idx = i
    max_idx = temp_diff.index(max(temp_diff))

    print(f"일교차가 가장 큰 날짜는 0000/00/00, 최대 일교차는 {max(temp_diff):.1f}")
    print(f"일교차가 가장 큰 날짜는{years[max_idx]}/{months[max_idx]:.02d}/{days[max_idx]:.02d}, 최대 일교차는 {max(temp_diff):.1f}입니다.")
    
    
    max_diff_date = dates[max_idx]
    max_diff_temp=0
    max_diff_date = None    #초기화하기/ 최대 온도 날짜 차이를 찾지 못했을 때를 대비
    for td, dates in zip(temp_diff,dates):
        if td>max_diff_temp:
            max_diff_temp=td
            max_diff_date= dates


    




if __name__ == "__main__":
    main()