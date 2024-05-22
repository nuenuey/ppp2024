import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

from hw16.big_to_small import toggle_text
def gui_input(text: str) -> str:
    return simpledialog.askstring(title="대<=>소문자 변환기", prompt=text)


def main():

    while True:

        text = gui_input(' 알파벳을 입력하시오: ')


        if text.isalpha():
            result = toggle_text(text)
            print(f"입력된 값은 {text}이고, 대소문자를 서로 변환하면 문자열은 {result}가 된다")
            break
        else:
            print("알파벳이 아닙니다.다시 입력해주시오.")

if __name__ == "__main__":
    main()
