from tkinter import *

THEME_COLOR = '#343951'
TEXT_COLOR = '#343951'
BUTTON_COLOR = '#13C2C2'
LABEL_COLOR = '#FA541C'
LABEL_FONT = ('Arial', 10, 'normal')

EURO_RATE_2020 = 4.61480
EURO_RATE_2019 = 4.2585
EURO_RATE_2018 = 4.3000
EURO_RATE_2017 = 4.1709


class Counter:
    def __init__(self):
        """Init main window with frame and canvas and add table"""
        self.window = Tk()
        self.window.title = 'Pito Counter'
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.row = -5
        self.added_company = False

        # Ogarnąc ten blok - START!!!

        self.container = Frame(self.window)
        self.canvas = Canvas(self.container, width=1400, height=600)
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
        self.canvas.grid(column=0, row=0, pady=40)
        self.scrollbar.grid(column=0, row=0, sticky='nes')

        # Ogarnąc ten blok - KONIEC!!!

        self.set_item_table()

        # Button - add new set of table
        self.add_button = Button(self.scrollable_frame, text='+', width=5, bg=BUTTON_COLOR, command=self.set_item_table)\
            .grid(column=11, row=5, pady=(5, 45))

        self.window.mainloop()

    def set_item_table(self):
        """Create table for data with labels and inputs"""
        self.row += 5
        if not self.added_company:
            self.added_company = True
        else:
            percent_label = Label(self.scrollable_frame, text='%: ', fg=TEXT_COLOR, font=LABEL_FONT)\
                .grid(column=0, row=self.row, pady=(40, 0))
            percent_input = Entry(self.scrollable_frame, width=10).grid(column=1, row=self.row, pady=(40, 0))
            self.row += 1

        # Year labels
        year_2020_label = Label(self.scrollable_frame, text='2020', fg=TEXT_COLOR, font=LABEL_FONT)\
            .grid(column=0, row=self.row + 1, padx=20)

        year_2019_label = Label(self.scrollable_frame, text='2019', fg=TEXT_COLOR, font=LABEL_FONT)\
            .grid(column=0, row=self.row + 2, padx=20)

        year_2018_label = Label(self.scrollable_frame, text='2018', fg=TEXT_COLOR, font=LABEL_FONT)\
            .grid(column=0, row=self.row + 3, padx=20)

        year_2017_label = Label(self.scrollable_frame, text='2017', fg=TEXT_COLOR, font=LABEL_FONT)\
            .grid(column=0, row=self.row + 4, padx=20)

        # Top labels

        euro_rate = Label(self.scrollable_frame, text='Kurs Euro', fg=TEXT_COLOR, font=LABEL_FONT)\
            .grid(column=1, row=self.row)

        income = Label(self.scrollable_frame, text='Przychody', fg=TEXT_COLOR, font=LABEL_FONT, pady=15)\
            .grid(column=2, row=self.row)

        income_euro = Label(self.scrollable_frame, text='Przychody euro', fg=TEXT_COLOR, font=LABEL_FONT, pady=15) \
            .grid(column=3, row=self.row)

        income_euro_thousand = Label(self.scrollable_frame, text='Przychody euro (tys.)', fg=TEXT_COLOR,
                                     font=LABEL_FONT, padx=15, pady=15).grid(column=4, row=self.row)

        income_euro_thousand_rounded = Label(self.scrollable_frame, text='Przychody euro (tys. zaokr.)', fg=TEXT_COLOR,
                                             font=LABEL_FONT).grid(column=5, row=self.row)

        balance = Label(self.scrollable_frame, text='Bilans', fg=TEXT_COLOR, font=LABEL_FONT, pady=15) \
            .grid(column=6, row=self.row)

        balance_euro = Label(self.scrollable_frame, text='Bilans euro', fg=TEXT_COLOR, font=LABEL_FONT, pady=15) \
            .grid(column=7, row=self.row)

        balance_euro_thousands = Label(self.scrollable_frame, text='Bilans euro (tys.)', fg=TEXT_COLOR, font=LABEL_FONT,
                                       pady=15).grid(column=8, row=self.row, padx=10)

        balance_euro_thousands_rounded = Label(self.scrollable_frame, text='Bilans euro (tys. zaokr.)', fg=TEXT_COLOR,
                                               font=LABEL_FONT, pady=15).grid(column=9, row=self.row, padx=10)

        employment = Label(self.scrollable_frame, text='Zatrudnienie', fg=TEXT_COLOR, font=LABEL_FONT, pady=15) \
            .grid(column=10, row=self.row, padx=10)

        # Euro rates labels

        euro_rate_2020 = Label(self.scrollable_frame, textvariable='4', text=EURO_RATE_2020, fg=LABEL_COLOR, font=LABEL_FONT)
        euro_rate_2020.grid(column=1, row=self.row + 1, padx=5)

        euro_rate_2019 = Label(self.scrollable_frame, text=EURO_RATE_2019, fg=LABEL_COLOR, font=LABEL_FONT) \
            .grid(column=1, row=self.row + 2, padx=5)

        euro_rate_2018 = Label(self.scrollable_frame, text=EURO_RATE_2018, fg=LABEL_COLOR, font=LABEL_FONT) \
            .grid(column=1, row=self.row + 3, padx=5)

        euro_rate_2017 = Label(self.scrollable_frame, text='4,1709', fg=LABEL_COLOR, font=LABEL_FONT) \
            .grid(column=1, row=self.row + 4, padx=5)

        # Year 2020

        income_var2020 = StringVar()
        income_var2020.trace_add("write", lambda name, index, mode, sv=income_var2020: update_income_labels
        (income_var2020, income_2020_euro, income_2020_euro_thousand, income_2020_euro_thousand_rounded, EURO_RATE_2020))

        income_2020 = Entry(self.scrollable_frame, width=20, textvariable=income_var2020)
        income_2020.grid(column=2, row=self.row + 1, padx=5, pady=5)

        income_2020_euro = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2020_euro.grid(column=3, row=self.row + 1)

        income_2020_euro_thousand = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2020_euro_thousand.grid(column=4, row=self.row + 1)

        income_2020_euro_thousand_rounded = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2020_euro_thousand_rounded.grid(column=5, row=self.row + 1)

        balance_var2020 = StringVar()
        balance_var2020.trace_add("write", lambda name, index, mode, sv=balance_var2020: update_balance_labels
        (balance_var2020, balance_euro_2020, balance_euro_thousands_2020, balance_euro_thousands_rounded_2020, EURO_RATE_2020))

        balance_2020 = Entry(self.scrollable_frame, width=20, textvariable=balance_var2020)
        balance_2020.grid(column=6, row=self.row + 1, padx=5, pady=5)

        balance_euro_2020 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_2020.grid(column=7, row=self.row + 1)

        balance_euro_thousands_2020 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_thousands_2020.grid(column=8, row=self.row + 1)

        balance_euro_thousands_rounded_2020 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_thousands_rounded_2020.grid(column=9, row=self.row + 1)

        employment_2020 = Entry(self.scrollable_frame, width=20).grid(column=10, row=self.row + 1, padx=5, pady=5)

        # Year 2019

        income_var2019 = StringVar()
        income_var2019.trace_add("write", lambda name, index, mode, sv=income_var2019: update_income_labels
        (income_var2019, income_2019_euro, income_2019_euro_thousand, income_2019_euro_thousand_rounded, EURO_RATE_2019))

        income_2019 = Entry(self.scrollable_frame, width=20, textvariable=income_var2019)
        income_2019.grid(column=2, row=self.row + 2, padx=5, pady=5)

        income_2019_euro = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2019_euro.grid(column=3, row=self.row + 2)

        income_2019_euro_thousand = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2019_euro_thousand.grid(column=4, row=self.row + 2)

        income_2019_euro_thousand_rounded = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2019_euro_thousand_rounded.grid(column=5, row=self.row + 2)

        balance_var2019 = StringVar()
        balance_var2019.trace_add("write", lambda name, index, mode, sv=balance_var2019: update_balance_labels
        (balance_var2019, balance_euro_2019, balance_euro_thousands_2019, balance_euro_thousands_rounded_2019,
         EURO_RATE_2019))

        balance_2019 = Entry(self.scrollable_frame, width=20, textvariable=balance_var2019)
        balance_2019.grid(column=6, row=self.row + 2, padx=5, pady=5)

        balance_euro_2019 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_2019.grid(column=7, row=self.row + 2)

        balance_euro_thousands_2019 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_thousands_2019.grid(column=8, row=self.row + 2)

        balance_euro_thousands_rounded_2019 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_thousands_rounded_2019.grid(column=9, row=self.row + 2)

        employment_2019 = Entry(self.scrollable_frame, width=20).grid(column=10, row=self.row + 2, padx=5, pady=5)

        # Year 2018

        income_var2018 = StringVar()
        income_var2018.trace_add("write", lambda name, index, mode, sv=income_var2018: update_income_labels
        (income_var2018, income_2018_euro, income_2018_euro_thousand, income_2018_euro_thousand_rounded, EURO_RATE_2018))

        income_2018 = Entry(self.scrollable_frame, width=20, textvariable=income_var2018)
        income_2018.grid(column=2, row=self.row + 3, padx=5, pady=5)

        income_2018_euro = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2018_euro.grid(column=3, row=self.row + 3)

        income_2018_euro_thousand = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2018_euro_thousand.grid(column=4, row=self.row + 3)

        income_2018_euro_thousand_rounded = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2018_euro_thousand_rounded.grid(column=5, row=self.row + 3)

        balance_var2018 = StringVar()
        balance_var2018.trace_add("write", lambda name, index, mode, sv=balance_var2018: update_balance_labels
        (balance_var2018, balance_euro_2018, balance_euro_thousands_2018, balance_euro_thousands_rounded_2018,
         EURO_RATE_2018))

        balance_2018 = Entry(self.scrollable_frame, width=20, textvariable=balance_var2018)
        balance_2018.grid(column=6, row=self.row + 3, padx=5, pady=5)

        balance_euro_2018 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_2018.grid(column=7, row=self.row + 3)

        balance_euro_thousands_2018 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_thousands_2018.grid(column=8, row=self.row + 3)

        balance_euro_thousands_rounded_2018 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_thousands_rounded_2018.grid(column=9, row=self.row + 3)

        employment_2018 = Entry(self.scrollable_frame, width=20).grid(column=10, row=self.row + 3, padx=5, pady=5)

        # Year 2017

        income_var2017 = StringVar()
        income_var2017.trace_add("write", lambda name, index, mode, sv=income_var2017: update_income_labels
        (income_var2017, income_2017_euro, income_2017_euro_thousand, income_2017_euro_thousand_rounded, EURO_RATE_2017))

        income_2017 = Entry(self.scrollable_frame, width=20, textvariable=income_var2017)
        income_2017.grid(column=2, row=self.row + 4, padx=5, pady=5)

        income_2017_euro = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2017_euro.grid(column=3, row=self.row + 4)

        income_2017_euro_thousand = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2017_euro_thousand.grid(column=4, row=self.row + 4)

        income_2017_euro_thousand_rounded = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2017_euro_thousand_rounded.grid(column=5, row=self.row + 4)

        balance_var2017 = StringVar()
        balance_var2017.trace_add("write", lambda name, index, mode, sv=balance_var2017: update_balance_labels
        (balance_var2017, balance_euro_2017, balance_euro_thousands_2017, balance_euro_thousands_rounded_2017,
         EURO_RATE_2017))

        balance_2017 = Entry(self.scrollable_frame, width=20, textvariable=balance_var2017)
        balance_2017.grid(column=6, row=self.row + 4, padx=5, pady=5)

        balance_euro_2017 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_2017.grid(column=7, row=self.row + 4)

        balance_euro_thousands_2017 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_thousands_2017.grid(column=8, row=self.row + 4)

        balance_euro_thousands_rounded_2017 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_euro_thousands_rounded_2017.grid(column=9, row=self.row + 4)

        employment_2017 = Entry(self.scrollable_frame, width=20).grid(column=10, row=self.row + 4, padx=5, pady=5)

        def update_income_labels(s_var, income_euro_input,
                                 income_euro_thousand_input, income_euro_thousand_rounded_input, actual_euro_rate):
            """Updates income labels with euro rate calculates"""
            income_in_euro = round(float(s_var.get()) * actual_euro_rate, 2)
            income_euro_input.config(text=income_in_euro)
            income_euro_thousand_input.config(text=income_in_euro / 1000)
            income_euro_thousand_rounded_input.config(text=round(income_in_euro / 1000, 2))

        def update_balance_labels(s_var, balance_euro_input,
                                 balance_euro_thousand_input, balance_euro_thousand_rounded_input, actual_euro_rate):
            """Updates balance labels with euro rate calculates"""
            balance_in_euro = round(float(s_var.get()) * actual_euro_rate, 2)
            balance_euro_input.config(text=balance_in_euro)
            balance_euro_thousand_input.config(text=balance_in_euro / 1000)
            balance_euro_thousand_rounded_input.config(text=round(balance_in_euro / 1000, 2))