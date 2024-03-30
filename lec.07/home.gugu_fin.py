def gugudan(dan):

    if dan>=1 and dan<=9 :
    
        
        for i in range(9):

            print(f"{i+1}*{dan}={(i+1)*dan}")
    else: 
        print("1에서 9까지의 숫자만 입력해주세요")

def main():
   dan=int(input("숫자를 입력하시오"))


   gugudan(dan)



if __name__ == "__main__":
    main()