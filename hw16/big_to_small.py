#아스키코드 65-90 대문자, 97-122 소문자

def toggle_text(text: str) -> str:
    toggled_text = ""



    for char in text:
        ascii_val = ord(char)#숫자
        if ascii_val >=97 and ascii_val <=122 :
            toggled_text += chr(ascii_val - 32)#문자




        elif ascii_val>=65 and ascii_val<=90 :
            toggled_text += chr(ascii_val + 32)  # 문자
        else:
            toggled_text += chr
    return toggled_text







def main():

    while True:
        text = input('대문자=>소문자, 소문자=>대문자 변환기. 알파벳을 입력하시오: ')


        if text.isalpha():
            result = toggle_text(text)
            print(f"입력된 값은 {text}이고, 대소문자를 서로 변환하면 문자열은 {result}가 된다")
            break
        else:
            print("알파벳이 아닙니다.다시 입력해주시오.")




if __name__ == "__main__":
    main()