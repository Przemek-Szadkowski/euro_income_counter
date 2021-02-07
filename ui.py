from tkinter import *

THEME_COLOR = '#343951'
TEXT_COLOR = '#343951'
BUTTON_COLOR = '#13C2C2'
LABEL_COLOR = '#FA541C'
LABEL_FONT = ('Arial', 12, 'normal')


class Counter:
    def __init__(self):
        self.window = Tk()
        self.window.title = 'Pito Counter'
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.row = -5
        self.added_company = False

        # Ogarnąc ten blok - START!!!

        self.container = Frame(self.window)
        self.canvas = Canvas(self.container, width=1000, height=700)
        self.scrollbar = Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.container.grid(column=0, row=0)
        self.canvas.grid(column=0, row=0)
        self.scrollbar.grid(column=0, row=0, sticky='nes')

        # Ogarnąc ten blok - KONIEC!!!

        self.set_item_table()

        self.add_button = Button(self.scrollable_frame, text='+', width=5, bg=BUTTON_COLOR, command=self.set_item_table)\
            .grid(column=7, row=5, pady=(5, 45))

        self.window.mainloop()

    def set_item_table(self):
        self.row += 5
        if not self.added_company:
            self.added_company = True
        else:
            percent_label = Label(self.scrollable_frame, text='%: ', fg=TEXT_COLOR, font=LABEL_FONT)\
                .grid(column=0, row=self.row)
            percent_input = Entry(self.scrollable_frame, width=10).grid(column=1, row=self.row)
            self.row += 1

        year_2020_label = Label(self.scrollable_frame, text='2020', fg=TEXT_COLOR, font=LABEL_FONT)\
            .grid(column=0, row=self.row + 1, padx=20)

        year_2019_label = Label(self.scrollable_frame, text='2019', fg=TEXT_COLOR, font=LABEL_FONT)\
            .grid(column=0, row=self.row + 2, padx=20)

        year_2018_label = Label(self.scrollable_frame, text='2018', fg=TEXT_COLOR, font=LABEL_FONT)\
            .grid(column=0, row=self.row + 3, padx=20)

        year_2017_label = Label(self.scrollable_frame, text='2017', fg=TEXT_COLOR, font=LABEL_FONT)\
            .grid(column=0, row=self.row + 4, padx=20)

        euro_rate_2020 = Label(self.scrollable_frame, text='Kurs Euro', fg=TEXT_COLOR, font=LABEL_FONT)\
            .grid(column=1, row=self.row)
        euro_rate_2020 = Label(self.scrollable_frame, text='4.61480', fg=LABEL_COLOR, font=LABEL_FONT)\
            .grid(column=1, row=self.row + 1, padx=5)

        income = Label(self.scrollable_frame, text='Przychody', fg=TEXT_COLOR, font=LABEL_FONT, pady=15)\
            .grid(column=2, row=self.row)

        income_2020 = Entry(self.scrollable_frame, width=20).grid(column=2, row=self.row + 1, padx=5, pady=5)

        income_euro = Label(self.scrollable_frame, text='Przychody euro', fg=TEXT_COLOR, font=LABEL_FONT, pady=15)\
            .grid(column=3, row=self.row)

        income_2020_euro = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)\
            .grid(column=3, row=self.row + 1)

        label = Label(self.scrollable_frame, text='Label_3', fg=TEXT_COLOR, font=LABEL_FONT, pady=15)\
            .grid(column=4, row=self.row)

        input_4 = Entry(self.scrollable_frame, width=20).grid(column=4, row=self.row + 1, padx=5, pady=5)

        label_4 = Label(self.scrollable_frame, text='Label_4', fg=TEXT_COLOR, font=LABEL_FONT, pady=15)\
            .grid(column=5, row=self.row)

        input_5 = Entry(self.scrollable_frame, width=20).grid(column=5, row=self.row + 1, padx=5, pady=5)

        label = Label(self.scrollable_frame, text='Label_5', fg=TEXT_COLOR, font=LABEL_FONT, pady=15)\
            .grid(column=6, row=self.row)

        input_6 = Entry(self.scrollable_frame, width=20).grid(column=6, row=self.row + 1, padx=5, pady=5)

        euro_rate_2019 = Label(self.scrollable_frame, text='4.2585', fg=LABEL_COLOR, font=LABEL_FONT) \
            .grid(column=1, row=self.row + 2, padx=5)

        income_2019 = Entry(self.scrollable_frame, width=20).grid(column=2, row=self.row + 2, padx=5, pady=5)

        income_2019_euro = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT) \
            .grid(column=3, row=self.row + 2)

        input_10 = Entry(self.scrollable_frame, width=20).grid(column=4, row=self.row + 2, padx=5, pady=5)

        input_11 = Entry(self.scrollable_frame, width=20).grid(column=5, row=self.row + 2, padx=5, pady=5)

        input_12 = Entry(self.scrollable_frame, width=20).grid(column=6, row=self.row + 2, padx=5, pady=5)

        euro_rate_2018 = Label(self.scrollable_frame, text='4,3000', fg=LABEL_COLOR, font=LABEL_FONT) \
            .grid(column=1, row=self.row + 3, padx=5)

        income_2018 = Entry(self.scrollable_frame, width=20).grid(column=2, row=self.row + 3, padx=5, pady=5)

        income_2018_euro = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT) \
            .grid(column=3, row=self.row + 3)

        input_16 = Entry(self.scrollable_frame, width=20).grid(column=4, row=self.row + 3, padx=5, pady=5)

        input_17 = Entry(self.scrollable_frame, width=20).grid(column=5, row=self.row + 3, padx=5, pady=5)

        input_18 = Entry(self.scrollable_frame, width=20).grid(column=6, row=self.row + 3, padx=5, pady=5)

        euro_rate_2017 = Label(self.scrollable_frame, text='4,1709', fg=LABEL_COLOR, font=LABEL_FONT) \
            .grid(column=1, row=self.row + 4, padx=5)

        income_2017 = Entry(self.scrollable_frame, width=20).grid(column=2, row=self.row + 4, padx=5, pady=5)

        income_2017_euro = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT) \
            .grid(column=3, row=self.row + 4)

        input_22 = Entry(self.scrollable_frame, width=20).grid(column=4, row=self.row + 4, padx=5, pady=5)

        input_23 = Entry(self.scrollable_frame, width=20).grid(column=5, row=self.row + 4, padx=5, pady=5)

        input_24 = Entry(self.scrollable_frame, width=20).grid(column=6, row=self.row + 4, padx=5, pady=5)
