from tkinter import *
from tkinter import ttk
from subprocess import call


# Кнопка "Правила"
def clicked_rules_btn():

    def go_back_rules():
        window_rules.destroy()
        window_menu.deiconify()

    window_menu.withdraw()

    window_rules = Tk()
    window_rules.title("Правила игры")
    window_rules.geometry('1920x1080')

    title_rules = Label(window_rules, text="Правила игры", font=("Calibri", 50))
    title_rules.place(relx=0.5, rely=0.2, anchor="c")

    text_rules1 = Label(window_rules,
                            text="Имеется игровое поле, на котором будет происходить действие игры. На данном поле случайным образом появляется еда (в виде кружочка, закрашенного красным цветом).",
                            font=('Calibri', 14))
    text_rules1.place(relx=0.5, rely=0.3, anchor='c')

    text_rules2 = Label(window_rules,
                            text="Есть змейка (связная последовательность из нескольких клеток, расположенных по прямой или с поворотами), которая постоянно двигается с момента запуска игры ",
                            font=('Calibri', 14))
    text_rules2.place(relx=0.5, rely=0.33, anchor='c')

    text_rules3 = Label(window_rules,
                            text="и является управляемой, при помощи стрелок на клавиатуре(вверх/вниз/вправо/влево). Если на пути у змейки появляется еда, то еда исчезает и тут же появляется на поле в другом месте, ",
                            font=('Calibri', 14))
    text_rules3.place(relx=0.5, rely=0.36, anchor='c')

    text_rules4 = Label(window_rules,
                            text="а сама змейка увеличивается на ОДНУ клеточку, а к счёту прибавляется 10 очков. ",
                            font=('Calibri', 14))
    text_rules4.place(relx=0.5, rely=0.39, anchor='c')

    text_rules5 = Label(window_rules,
                            text="Цель игры - накормить змейку, сделав её как можно длиннее.",
                            font=('Calibri', 14))
    text_rules5.place(relx=0.5, rely=0.42, anchor='c')

    text_rules5 = Label(window_rules,
                            text="Игра оканчивается, когда змейка врезается в стену или в саму себя. (Стеной являются края игрового поля)",
                            font=('Calibri', 14))
    text_rules5.place(relx=0.5, rely=0.45, anchor='c')

    go_btn = ttk.Button(window_rules, text="<---", command=go_back_rules)
    go_btn.place(x=0, y=0, anchor="nw", width=80, height=40)

    window_rules.mainloop()

# Кнопка "Выход"
def clicked_exit_btn():
    window_menu.destroy()

# Кнопка "Играть"
#def clicked_play_btn():
    #window_menu.withdraw()
    #call(["python", "play.py"])


if __name__ == '__main__':

    # Настройка окна меню
    window_menu = Tk()
    window_menu.title("Змейка")
    window_menu.geometry('1920x1080')

    title = ttk.Label(window_menu, text="Меню", font=("Calibri", 50))
    title.place(relx=0.5, rely=0.3, anchor="c")

    play_btn = ttk.Button(text="Играть")
    play_btn.place(relx=0.5, rely=0.4, anchor="c", width=80, height=40)

    rules_btn = ttk.Button(text="Правила", command=clicked_rules_btn)
    rules_btn.place(relx=0.5, rely=0.5, anchor="c", width=80, height=40)

    exit_btn = ttk.Button(text="Выйти", command=clicked_exit_btn)
    exit_btn.place(relx=0.5, rely=0.6, anchor="c", width=80, height=40)

    window_menu.mainloop()




