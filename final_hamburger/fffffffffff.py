import tkinter as tk
import random
from tkinter import messagebox

stack = []
current_order_key = ""
correct_order = []

orders = {
    '요청사항 없음': ["번", "소스", "패티", "양파", "피클", "양상추", "소스", "번"],
    '피클 빼주세요.': ["번", "소스", "패티", "양파", "양상추", "소스", "번"],
    '양파 빼주세요.': ["번", "소스", "패티", "피클", "양상추", "소스", "번"],
    '피클, 양파 빼주세요.': ["번", "소스", "패티", "양상추", "소스", "번"],
    '소스 빼주세요.': ["번", "패티", "양파", "피클", "양상추", "번"],
    '더블 패티로 해주세요.': ["번", "소스", "패티", "패티", "양파", "피클", "양상추", "소스", "번"],
}


def set_new_order(label_order):
    global current_order_key, correct_order
    order_memo_list = list(orders.keys())
    current_order_key = random.choice(order_memo_list)
    correct_order = orders[current_order_key]
    label_order.config(text=f"요청사항: {current_order_key}")


def add_ingredient(ingredient):
    stack.append(ingredient)
    update_display()


def update_display():
    hamburger_display.delete(1.0, tk.END)
    for ingredient in reversed(stack):
        hamburger_display.insert(tk.END, ingredient + "\n")


def finish_hamburger():
    global stack, correct_order
    print(f"ㅇㅇㅇㅇstack: {stack}")
    print(f"ㅇㅇㅇㅇorder: {correct_order}")

    if stack == correct_order:
        messagebox.showinfo("성공", "햄버거 나왔습니다!")
    else:
        messagebox.showerror("실패", "잘못 만들었네요. 다시 만들겠습니다.")

    stack.clear()
    set_new_order(label_order)
    update_display()


def reset_screen():
    stack.clear()
    hamburger_display.delete(1.0, tk.END)
    set_new_order(label_order)
    update_display()


def create_main_window():
    global hamburger_display, label_order

    window = tk.Tk()
    window.title("햄버거 만들기")
    window.resizable(width=False, height=False)

    label = tk.Label(window, text="햄버거 만들기", font=("Helvetica", 16))
    label.pack(pady=10)

    label_order = tk.Label(window, font=("Helvetica", 10))
    label_order.pack(pady=10)
    set_new_order(label_order)




    recipes = tk.Label(window, text="햄버거 레시피 : 번, 소스, 패티, 양파, 피클, 양상추, 소스, 번 순", font=("Helvetica", 10), fg="brown")
    recipes.pack()

    btn_bun = tk.Button(window, text="번 추가", bg="beige", fg="black", command=add_bun)
    btn_bun.pack(pady=5)

    btn_sauce = tk.Button(window, text="소스 추가", bg="yellow", fg="black", command=add_sauce)
    btn_sauce.pack(pady=5)

    btn_patty = tk.Button(window, text="패티 추가", bg="brown", fg="yellow", command=add_patty)
    btn_patty.pack(pady=5)

    btn_onion = tk.Button(window, text="양파 추가", command=add_onion)
    btn_onion.pack(pady=5)

    btn_pickle = tk.Button(window, text="피클 추가", bg="green", fg="yellow", command=add_pickle)
    btn_pickle.pack(pady=5)

    btn_lettuce = tk.Button(window, text="양상추 추가", bg="lightgreen", fg="white", command=add_lettuce)
    btn_lettuce.pack(pady=5)

    btn_finish = tk.Button(window, text="완성", bg="black", fg="yellow", command=finish_hamburger)
    btn_finish.pack(pady=10)

    btn_reset = tk.Button(window, text="리셋", bg="white", fg="black", command=reset_screen)
    btn_reset.pack(pady=10)

    hamburger_display = tk.Text(window, height=7, width=30)
    hamburger_display.pack(pady=10)

    window.mainloop()


def add_bun():
    add_ingredient("번")


def add_sauce():
    add_ingredient("소스")


def add_patty():
    add_ingredient("패티")


def add_onion():
    add_ingredient("양파")


def add_pickle():
    add_ingredient("피클")


def add_lettuce():
    add_ingredient("양상추")


create_main_window()
