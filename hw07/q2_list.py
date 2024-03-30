#1-n까지 리스트를 돌려주는 함수를 만드시오
def get_range_list(n):
     
    return list(range(0, n))
def main():

    numbers=[]
#입력받을 n개의 숫자 정하기
    n= int(input("숫자 개수를 입력하시오"))

    for i in range(n):
        num = int(input(f"{i+1}번째 숫자를 입력하시오 :"))
        numbers.append(num)
    
    print(f"입력한 리스트 값을 출력하시오 {numbers}")

#입력받은 숫자를 리스트에 저장하기

if __name__ == "__main__":
    main()
