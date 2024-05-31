import tkinter as tk

def create_triangle():
    #*로 삼각형
    try:
        n = int(ent_layers.get())
        if n == 1:
            lbl_result["text"] = "다시 입력하시오. 1개의 *로는 삼각형을 만들 수 없습니다."
        else:
            result = ""
            total = 0
            for i in range(n):
                total += (i + 1)
                result += "*" * total + "\n"
            lbl_result["text"] = result
    except ValueError:
        lbl_result["text"] = "유효한 숫자를 입력하세요."


window = tk.Tk()
window.title("*로 삼각형 만들기")
window.resizable(width=False, height=False)# 배경크기 False면고정


label = tk.Label(text="몇 층의 *삼각형을 만들까요? 입력하고 버튼을 누르세요:")
label.pack(padx=10, pady=10)


frm_entry = tk.Frame(master=window)
ent_layers = tk.Entry(master=frm_entry, width=10)#  층 수를 입력 받음
lbl_layers = tk.Label(master=frm_entry, text="층 수")#  층 수를 입력 받음
ent_layers.grid(row=0, column=0, sticky="e")
lbl_layers.grid(row=0, column=1, sticky="w")
frm_entry.pack(padx=10, pady=10)


btn_convert = tk.Button(#버튼 추가
    master=window,
    text="Create Triangle",
    bg="blue",
    fg="yellow",
    command=create_triangle
)
lbl_result = tk.Label(master=window, text="")#lbl_result 레이블을 사용하여 결과를 표시


btn_convert.pack(padx=10, pady=10)
lbl_result.pack(padx=10, pady=10)

window.mainloop()

