import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

import random

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="로또번호 추출기", prompt=text)
def get_lotto():
    results = []

    while len(results) < 6:  # 결과가 6개가 될 때까지 반복
        num = random.randint(1, 45)
        if num not in results:
            results.append(num)

    return sorted(results)
    # return [3,5,8,10, 12, 15]


def main():
    count = int(gui_input("로또번호 추출하기!!  몇 개를 추출할까요? "))

    for i in range(count):
        lotto_nums = get_lotto()
        print(f"{i + 1} : {lotto_nums}")


if __name__ == "__main__":
    main()