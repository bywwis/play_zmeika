from tkinter import *
import random

# Меню
def Menu():
    title = Label(window, text="Меню", font=("Calibri", 50))
    title.grid(column=0, row=0)

    play_btn = Button(window, text="Играть", font="Calibri")
    play_btn.configure(width=12, height=2)
    play_btn.grid(column=1, row=1)

    rules_btn = Button(window, text="Правила", font="Calibri")
    rules_btn.configure(width=12, height=2)
    rules_btn.grid(column=2, row=2)





if __name__ == '__main__':
    # Настройка окна
    window = Tk()
    window.title("Змейка")
    window.geometry('1920x1080')
    Menu()
    window.mainloop()




