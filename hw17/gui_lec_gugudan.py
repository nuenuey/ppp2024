import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()
import random

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="구구단 게임", prompt=text)
def get_number():
    results = []
    while True:
        num = random.randint(1, 9)
        if num not in results:
            results.append(num)
            return num

def main():
    count = 5

    correct_answers = 0
    print("구구단게임 시작합니다!!. 총 5문제입니다")
    for i in range(count):
        num1 = get_number()
        num2 = get_number()
        correct = num1 * num2

        answer = int(gui_input(f"구구단문제.{num1}*{num2} =?"))
        if answer == correct:
                print("정답입니다")
                correct_answers += 1
        else:
                print(f"오답입니다. 정답은{correct}입니다. ")

    if correct_answers==5:
        print("100점입니다.")
    elif correct_answers==4:
        print("80점입니다.")
    elif correct_answers==3:
        print("60점입니다.")
    elif correct_answers==2:
        print("40점입니다.")
    elif correct_answers==1:
        print("20점입니다.")
    elif correct_answers==0:
        print("0점입니다.")



if __name__ == "__main__":
    main()
