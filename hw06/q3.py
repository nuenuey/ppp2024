#섭씨를 화씨로 바꾸는 함수 c2f(t_c) 함수를 만드시오

def c2f(t_c):
    return  (t_c)/ 1.8 +32

def main():
    t_c= int(input("$섭씨 => 화씨 계산기$ 섭씨온도를 입력하시오."))

    print(f"{t_c}℃ => {c2f(t_c)}℉")

if __name__ == "__main__":
    main()