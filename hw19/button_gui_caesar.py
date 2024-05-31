import tkinter as tk

def caesar_encode():
    try:
        text= ent_temperature.get()
        if len(text) == 3 and text.isalpha():
            shift = 3
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
            lbl_result["text"] = encoding_text
        else:
            lbl_result["text"] = "다시 입력하시오"
    except ValueError:
        pass

window = tk.Tk()
window.title("카이사르")
window.resizable(width=30, height=30) #배경크기 False면고정

label = tk.Label(text='영어로 된 문자열 3개 000을 입력하시오:')
label.pack()


frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="인코딩")
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")
frm_entry.pack(padx=10, pady=10)

btn_convert = tk.Button(
    master=window,
    text="===Shift3==>>>>",
    bg="purple",
    fg="yellow",
    command=caesar_encode
)
lbl_result = tk.Label(master=window, text="디코딩")

btn_convert.pack(padx=10, pady=20)#버튼 padx는 가로 여백, pady는 세로 여백
lbl_result.pack(padx=150, pady=10)  #라벨
window.mainloop()
