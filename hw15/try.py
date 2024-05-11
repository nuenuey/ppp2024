num_list=[]
while True:
    try:# try--- 예외가 일어날 수 있는 코드
            #num_list=[]
        num = int(input('자연수를 입력해 주세요:')) #.split()여러개 입력
        if num == -1:
            break
        if num <= 0:
            print('입력한 값은 자연수가 아닙니다.')
        else:
            num_list.append(num)
        #print(num_list)
    except ValueError:# int 유형이 될 수 없는--------- 문자열 오류 처리
        print('입력한 값은 정수가 아닙니다.')
    #except num<=0: #음수 오류처리
    #    if num <= 0:
    #        print('입력한 값은 자연수가 아닙니다.')

def main():

    print(f"입력된 값은 {num_list}입니다. 총 {len(num_list)}개의 자연수가 입력되었고, 평균은 {(sum(num_list)) / len(num_list)} 입니다.")

if __name__ == "__main__":
    main()