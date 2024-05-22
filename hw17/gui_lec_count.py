import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()
import time

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="카운팅", prompt=text)


def main():
    count = int(gui_input("카운트다운!! 몇 초를 셀까요? "))

    while True:
        print(f"{count}")

        time.sleep(1)
        count -= 1
        if count <= 0:
            break
    print()
    print("bomb!!!")


if __name__ == "__main__":
    main()