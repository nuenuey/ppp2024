import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
label = tk.Label(text="Name")
entry = tk.Entry()
window.withdraw()

label.pack()
entry.pack()
answer = entry.get()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="카이사르 계산기", prompt=text)
def caesar_encode(text: str, shift: int = 3) -> str:
    encoding_text = ""

    for char in text:
        #알파벳 = 26 z후 다시 a로 돌아오기위해
        #ord(char) 문자를 ASCII 값으로 변환
        #ex) ord('A') 65....

        if char.isupper(): #대문자
            encoding_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))

        elif char.islower(): #소문자

            encoding_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:

            encoding_text += char
    return encoding_text





def main(): #입력장치
    while True:
        text = gui_input('영어로 된 문자열 3개 000을 입력하시오: ')
        encoded_text = caesar_encode(text) #ABC

        if len(text) == 3 and text.isalpha():

            print(f"{text}의 3칸 밀린 칸은(카이사르 값은)? {encoded_text}입니다.")  # 출력: DEF
            break
        else:
            print("다시 입력해주시오.")





if __name__ == "__main__":
    main()