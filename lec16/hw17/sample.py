import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()


def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Input", prompt=text)


def main():
    USER_INP = gui_input("What's your Name?")
    print("Hello", USER_INP)

if __name__ == "__main__":
    main()
