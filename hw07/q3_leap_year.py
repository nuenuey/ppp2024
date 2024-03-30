
def  is_leap_year(y):
    
    if y % 4 == 0:
        if y % 100 == 0:
            print("F : 윤년이 아님")
        else:
            print("T : 윤년임")
    else:
        print("F : 윤년이 아님")  
       
       
       
def main():
    year= int(input("$윤년 T/F 계산기$// 연도를 입력하시오"))
    result = is_leap_year(year)
    


if __name__ == "__main__":
    main()