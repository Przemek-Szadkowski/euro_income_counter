from tkinter import *

THEME_COLOR = '#343951'
TEXT_COLOR = '#FA541C'
INPUT_COLOR = '#13C2C2'
LABEL_FONT = ('Courier', 14, 'bold')


class Counter:
    def __init__(self):
        self.window = Tk()
        self.window.title = 'Pito Counter'
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.row = -4
        self.set_item_table()
        self.add_button = Button(text='+', width=2, bg=TEXT_COLOR, comman=self.set_item_table)
        self.add_button.grid(column=0, row=3)

        self.window.mainloop()

    def set_item_table(self):
        self.row += 4
        label = Label(text='Label_1', fg=TEXT_COLOR, bg=THEME_COLOR, font=LABEL_FONT, pady=15)
        label.grid(column=0, row=self.row)

        input_1 = Entry(width=20)
        input_1.config(bg=INPUT_COLOR)
        input_1.grid(column=0, row=self.row + 1, padx=5, pady=5)

        label = Label(text='Label_2', fg=TEXT_COLOR, bg=THEME_COLOR, font=LABEL_FONT, pady=15)
        label.grid(column=1, row=self.row)

        input_2 = Entry(width=20)
        input_2.config(bg=INPUT_COLOR)
        input_2.grid(column=1, row=self.row + 1, padx=5, pady=5)

        label = Label(text='Label_2', fg=TEXT_COLOR, bg=THEME_COLOR, font=LABEL_FONT, pady=15)
        label.grid(column=2, row=self.row)

        input_3 = Entry(width=20)
        input_3.config(bg=INPUT_COLOR)
        input_3.grid(column=2, row=self.row + 1, padx=5, pady=5)

        label = Label(text='Label_3', fg=TEXT_COLOR, bg=THEME_COLOR, font=LABEL_FONT, pady=15)
        label.grid(column=3, row=self.row)

        input_4 = Entry(width=20)
        input_4.config(bg=INPUT_COLOR)
        input_4.grid(column=3, row=self.row + 1, padx=5, pady=5)

        label = Label(text='Label_4', fg=TEXT_COLOR, bg=THEME_COLOR, font=LABEL_FONT, pady=15)
        label.grid(column=4, row=self.row)

        input_5 = Entry(width=20)
        input_5.config(bg=INPUT_COLOR)
        input_5.grid(column=4, row=self.row + 1, padx=5, pady=5)

        label = Label(text='Label_5', fg=TEXT_COLOR, bg=THEME_COLOR, font=LABEL_FONT, pady=15)
        label.grid(column=5, row=self.row)

        input_6 = Entry(width=20)
        input_6.config(bg=INPUT_COLOR)
        input_6.grid(column=5, row=self.row + 1, padx=5, pady=5)

        input_7 = Entry(width=20)
        input_7.config(bg=INPUT_COLOR)
        input_7.grid(column=0, row=self.row + 2, padx=5, pady=5)

        input_8 = Entry(width=20)
        input_8.config(bg=INPUT_COLOR)
        input_8.grid(column=1, row=self.row + 2, padx=5, pady=5)

        input_9 = Entry(width=20)
        input_9.config(bg=INPUT_COLOR)
        input_9.grid(column=2, row=self.row + 2, padx=5, pady=5)

        input_10 = Entry(width=20)
        input_10.config(bg=INPUT_COLOR)
        input_10.grid(column=3, row=self.row + 2, padx=5, pady=5)

        input_11 = Entry(width=20)
        input_11.config(bg=INPUT_COLOR)
        input_11.grid(column=4, row=self.row + 2, padx=5, pady=5)

        input_12 = Entry(width=20)
        input_12.config(bg=INPUT_COLOR)
        input_12.grid(column=5, row=self.row + 2, padx=5, pady=5)
