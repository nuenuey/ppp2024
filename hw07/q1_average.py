# 숫자 리스트를 매개변수로 받아, 평균을 구하기

def average(numbers):
#리스트 [0] ~[n]의 평균 값 구하기
    
    n=len(numbers)
    total= sum(numbers)
    
    return total / n


def main():

    numbers=[]
#입력받을 n개의 숫자 정하기
    n= int(input("숫자 개수를 입력하시오"))

    for i in range(n):
        num = int(input(f"{i+1}번째 숫자를 입력하시오 :"))
        numbers.append(num)

    print(f"리스트{numbers}의 평균 값은? {average(numbers)} 입니다.")
    result=average(numbers)
#입력받은 숫자를 리스트에 저장하기


if __name__ == "__main__":
    main()












