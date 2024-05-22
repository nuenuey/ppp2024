import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

from hw16.caesar_shift import caesar_encode

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="카이사르 계산기", prompt=text)


def main():
    while True:
        text = gui_input('영어로 된 문자열 3개 000을 입력하시오: ')
        encoded_text = caesar_encode(text)  # ABC

        if len(text) == 3 and text.isalpha():

            print(f"{text}의 3칸 밀린 칸은(카이사르 값은)? {encoded_text}입니다.")  # 출력: DEF
            break
        else:
            print("다시 입력해주시오.")


if __name__ == "__main__":
    main()
