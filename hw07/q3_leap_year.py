
def  is_leap_year(y):
    
  
    if  y % 4 == 0 and y%100!=0:
        return True
    return False
       
       
def main():
    year= int(input("$윤년 T/F 계산기$// 연도를 입력하시오"))
    result = is_leap_year(year)
    
    if result:
        print(f"{year}년은 윤년입니다.")
    else:
        print(f"{year}년은 윤년이 아닙니다.")


if __name__ == "__main__":
    main()