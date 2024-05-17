def caesar_encode(text: str, shift: int = 3) -> str:
    encoding_text = ""

    for char in text:

        if char.isupper():
            encoding_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))

        elif char.islower():

            encoding_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:

            encoding_text += char
    return encoding_text





def main():
    while True:
        text = input('영어로 된 문자열 3개 000을 입력하시오: ')
        encoded_text = caesar_encode(text) #ABC

        if len(text) == 3 and text.isalpha():

            print(f"{text}의 3칸 밀린 칸은(카이사르 값은)? {encoded_text}입니다.")  # 출력: DEF
            break
        else:
            print("다시 입력해주시오.")





if __name__ == "__main__":
    main()