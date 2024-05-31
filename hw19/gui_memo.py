#라벨과 버튼 위젯으로 텍스트 입력을 수집가능
label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
#Button위젯
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
#Entry위젯 - 작은 텍스트 상자 //텍스트 검색.get(), 텍스트 삭제.delete(), 텍스트 삽입.insert()
import tkinter as tk
window = tk.Tk()
label = tk.Label(text="Name")
entry = tk.Entry()

label.pack()
entry.pack()
name = entry.get()
name #입력갓
#Text위젯
window = tk.Tk()
text_box = tk.Text()
text_box.pack()