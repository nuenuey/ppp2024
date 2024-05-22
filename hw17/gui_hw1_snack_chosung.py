import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()
import random
from hw16.snack_chosung_game import get_chosung

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="과자 초성 맞추기", prompt=text)


def main():

    hidden_answer_list = ["빅파이", "초코파이", "화이트하임", "초코송이", "새우깡", "감자깡", "먹태깡", "꼬북칩", "빈츠", "고래밥"]
    choicelist = random.choice(hidden_answer_list)
    # print(choicelist)
    problem = get_chosung(choicelist)  # ㅍㅇㅅ
    print(f"과자 이름 맞추기 게임입니다!! 주어진 초성은 '{''.join(problem)}'입니다. 정답을 입력해주세요.")
    while True:
        answer = gui_input("답은=>?")
        if answer == choicelist:
            print("정답입니다")
            break
        else:
            print("틀렸습니다. 다시시도하시오.")




if __name__ == "__main__":
    main()
