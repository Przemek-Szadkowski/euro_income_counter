from tkinter import *

THEME_COLOR = '#343951'
TEXT_COLOR = '#343951'
BUTTON_AND_PERCENT_COLOR = '#EDCD68'
RESULT_COLOR = '#8A9DFF'
LABEL_COLOR = '#FA541C'
LABEL_FONT = ('Arial', 10, 'normal')

EURO_RATE_2020 = 4.61480
EURO_RATE_2019 = 4.2585
EURO_RATE_2018 = 4.3000
EURO_RATE_2017 = 4.1709

YEAR_2020 = '2020'
YEAR_2019 = '2019'
YEAR_2018 = '2018'
YEAR_2017 = '2017'


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
        self.canvas = Canvas(self.container, width=1450, height=500)
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

        self.result = {
            '2020': {
                'Kurs Euro': EURO_RATE_2020,
                'Przychody': 0,
                'Przychody złoty': 0,
                'Przychody złoty (tys.)': 0,
                "Przychody złoty (tys. zaokr.)": 0,
                'Bilans': 0,
                'Bilans złoty': 0,
                'Bilans złoty (tys.)': 0,
                'Bilans złoty (tys. zaokr.)': 0,
                'Zatrudnienie': 0,
            },
            '2019': {
                'Kurs Euro': EURO_RATE_2019,
                'Przychody': 0,
                'Przychody złoty': 0,
                'Przychody złoty (tys.)': 0,
                "Przychody złoty (tys. zaokr.)": 0,
                'Bilans': 0,
                'Bilans złoty': 0,
                'Bilans złoty (tys.)': 0,
                'Bilans złoty (tys. zaokr.)': 0,
                'Zatrudnienie': 0,
            },
            '2018': None,
            '2017': None,
        }
        self.set_item_table()

        # Button - add new set of table
        self.add_button = Button(self.container, text='+', width=10, bg=BUTTON_AND_PERCENT_COLOR, command=self.set_item_table)\
            .grid(sticky='e', padx=(0, 50), pady=(0, 5))

        self.set_result_table()

        self.window.mainloop()

    def set_item_table(self):
        """Create table for data with labels and inputs"""
        self.row += 5
        if not self.added_company:
            self.added_company = True
        else:
            percent_label = Label(self.scrollable_frame, text='%: ', fg=TEXT_COLOR, font=LABEL_FONT)\
                .grid(column=0, row=self.row, pady=(20, 0))
            percent_input = Entry(self.scrollable_frame, width=10, bg=BUTTON_AND_PERCENT_COLOR).grid(column=1, row=self.row, pady=(20, 0))
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

        income_zloty = Label(self.scrollable_frame, text='Przychody zloty', fg=TEXT_COLOR, font=LABEL_FONT, pady=15) \
            .grid(column=3, row=self.row)

        income_zloty_thousand = Label(self.scrollable_frame, text='Przychody zloty (tys.)', fg=TEXT_COLOR,
                                     font=LABEL_FONT, padx=15, pady=15).grid(column=4, row=self.row)

        income_zloty_thousand_rounded = Label(self.scrollable_frame, text='Przychody zloty (tys. zaokr.)', fg=TEXT_COLOR,
                                             font=LABEL_FONT).grid(column=5, row=self.row)

        balance = Label(self.scrollable_frame, text='Bilans', fg=TEXT_COLOR, font=LABEL_FONT, pady=15) \
            .grid(column=6, row=self.row)

        balance_zloty = Label(self.scrollable_frame, text='Bilans zloty', fg=TEXT_COLOR, font=LABEL_FONT, pady=15) \
            .grid(column=7, row=self.row)

        balance_zloty_thousands = Label(self.scrollable_frame, text='Bilans zloty (tys.)', fg=TEXT_COLOR, font=LABEL_FONT,
                                       pady=15).grid(column=8, row=self.row, padx=10)

        balance_zloty_thousands_rounded = Label(self.scrollable_frame, text='Bilans zloty (tys. zaokr.)', fg=TEXT_COLOR,
                                               font=LABEL_FONT, pady=15).grid(column=9, row=self.row, padx=10)

        employment = Label(self.scrollable_frame, text='Zatrudnienie', fg=TEXT_COLOR, font=LABEL_FONT, pady=15)\
            .grid(column=10, row=self.row, padx=10)

        # Euro rates labels

        euro_rate_2020 = Label(self.scrollable_frame, textvariable='4', text=EURO_RATE_2020, fg=LABEL_COLOR, font=LABEL_FONT)
        euro_rate_2020.grid(column=1, row=self.row + 1, padx=5)

        euro_rate_2019 = Label(self.scrollable_frame, text=EURO_RATE_2019, fg=LABEL_COLOR, font=LABEL_FONT)
        euro_rate_2019.grid(column=1, row=self.row + 2, padx=5)

        euro_rate_2018 = Label(self.scrollable_frame, text=EURO_RATE_2018, fg=LABEL_COLOR, font=LABEL_FONT)
        euro_rate_2018.grid(column=1, row=self.row + 3, padx=5)

        euro_rate_2017 = Label(self.scrollable_frame, text='4,1709', fg=LABEL_COLOR, font=LABEL_FONT)
        euro_rate_2017.grid(column=1, row=self.row + 4, padx=5)

        # Year 2020

        income_var2020 = StringVar()
        income_var2020.trace_add("write", lambda name, index, mode, sv=income_var2020: update_income_labels
        (income_var2020, income_2020_zloty, income_2020_zloty_thousand, income_2020_zloty_thousand_rounded, EURO_RATE_2020))

        income_2020 = Entry(self.scrollable_frame, width=20, textvariable=income_var2020)
        income_2020.grid(column=2, row=self.row + 1, padx=5, pady=5)

        income_2020_zloty = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2020_zloty.grid(column=3, row=self.row + 1)

        income_2020_zloty_thousand = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2020_zloty_thousand.grid(column=4, row=self.row + 1)

        income_2020_zloty_thousand_rounded = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2020_zloty_thousand_rounded.grid(column=5, row=self.row + 1)

        balance_var2020 = StringVar()
        balance_var2020.trace_add('write', lambda name, index, mode, sv=balance_var2020: update_balance_labels
        (balance_var2020, balance_zloty_2020, balance_zloty_thousands_2020, balance_zloty_thousands_rounded_2020, EURO_RATE_2020))

        balance_2020 = Entry(self.scrollable_frame, width=20, textvariable=balance_var2020)
        balance_2020.grid(column=6, row=self.row + 1, padx=5, pady=5)

        balance_zloty_2020 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_2020.grid(column=7, row=self.row + 1)

        balance_zloty_thousands_2020 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_thousands_2020.grid(column=8, row=self.row + 1)

        balance_zloty_thousands_rounded_2020 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_thousands_rounded_2020.grid(column=9, row=self.row + 1)

        employment_var2020 = StringVar()
        employment_var2020.trace_add('write', lambda name, index, mode, sv=employment_var2020: update_employment_status(employment_var2020))
        employment_2020 = Entry(self.scrollable_frame, width=20, textvariable=employment_var2020)
        employment_2020.grid(column=10, row=self.row + 1, padx=5, pady=5)

        # Year 2019

        income_var2019 = StringVar()
        income_var2019.trace_add("write", lambda name, index, mode, sv=income_var2019: update_income_labels
        (income_var2019, income_2019_zloty, income_2019_zloty_thousand, income_2019_zloty_thousand_rounded, EURO_RATE_2019))

        income_2019 = Entry(self.scrollable_frame, width=20, textvariable=income_var2019)
        income_2019.grid(column=2, row=self.row + 2, padx=5, pady=5)

        income_2019_zloty = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2019_zloty.grid(column=3, row=self.row + 2)

        income_2019_zloty_thousand = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2019_zloty_thousand.grid(column=4, row=self.row + 2)

        income_2019_zloty_thousand_rounded = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2019_zloty_thousand_rounded.grid(column=5, row=self.row + 2)

        balance_var2019 = StringVar()
        balance_var2019.trace_add("write", lambda name, index, mode, sv=balance_var2019: update_balance_labels
        (balance_var2019, balance_zloty_2019, balance_zloty_thousands_2019, balance_zloty_thousands_rounded_2019,
         EURO_RATE_2019))

        balance_2019 = Entry(self.scrollable_frame, width=20, textvariable=balance_var2019)
        balance_2019.grid(column=6, row=self.row + 2, padx=5, pady=5)

        balance_zloty_2019 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_2019.grid(column=7, row=self.row + 2)

        balance_zloty_thousands_2019 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_thousands_2019.grid(column=8, row=self.row + 2)

        balance_zloty_thousands_rounded_2019 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_thousands_rounded_2019.grid(column=9, row=self.row + 2)

        employment_2019 = Entry(self.scrollable_frame, width=20)
        employment_2019.grid(column=10, row=self.row + 2, padx=5, pady=5)

        # Year 2018

        income_var2018 = StringVar()
        income_var2018.trace_add("write", lambda name, index, mode, sv=income_var2018: update_income_labels
        (income_var2018, income_2018_zloty, income_2018_zloty_thousand, income_2018_zloty_thousand_rounded, EURO_RATE_2018))

        income_2018 = Entry(self.scrollable_frame, width=20, textvariable=income_var2018)
        income_2018.grid(column=2, row=self.row + 3, padx=5, pady=5)

        income_2018_zloty = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2018_zloty.grid(column=3, row=self.row + 3)

        income_2018_zloty_thousand = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2018_zloty_thousand.grid(column=4, row=self.row + 3)

        income_2018_zloty_thousand_rounded = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2018_zloty_thousand_rounded.grid(column=5, row=self.row + 3)

        balance_var2018 = StringVar()
        balance_var2018.trace_add("write", lambda name, index, mode, sv=balance_var2018: update_balance_labels
        (balance_var2018, balance_zloty_2018, balance_zloty_thousands_2018, balance_zloty_thousands_rounded_2018,
         EURO_RATE_2018))

        balance_2018 = Entry(self.scrollable_frame, width=20, textvariable=balance_var2018)
        balance_2018.grid(column=6, row=self.row + 3, padx=5, pady=5)

        balance_zloty_2018 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_2018.grid(column=7, row=self.row + 3)

        balance_zloty_thousands_2018 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_thousands_2018.grid(column=8, row=self.row + 3)

        balance_zloty_thousands_rounded_2018 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_thousands_rounded_2018.grid(column=9, row=self.row + 3)

        employment_2018 = Entry(self.scrollable_frame, width=20).grid(column=10, row=self.row + 3, padx=5, pady=5)

        # Year 2017

        income_var2017 = StringVar()
        income_var2017.trace_add("write", lambda name, index, mode, sv=income_var2017: update_income_labels
        (income_var2017, income_2017_zloty, income_2017_zloty_thousand, income_2017_zloty_thousand_rounded, EURO_RATE_2017))

        income_2017 = Entry(self.scrollable_frame, width=20, textvariable=income_var2017)
        income_2017.grid(column=2, row=self.row + 4, padx=5, pady=5)

        income_2017_zloty = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2017_zloty.grid(column=3, row=self.row + 4)

        income_2017_zloty_thousand = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2017_zloty_thousand.grid(column=4, row=self.row + 4)

        income_2017_zloty_thousand_rounded = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        income_2017_zloty_thousand_rounded.grid(column=5, row=self.row + 4)

        balance_var2017 = StringVar()
        balance_var2017.trace_add("write", lambda name, index, mode, sv=balance_var2017: update_balance_labels
        (balance_var2017, balance_zloty_2017, balance_zloty_thousands_2017, balance_zloty_thousands_rounded_2017,
         EURO_RATE_2017))

        balance_2017 = Entry(self.scrollable_frame, width=20, textvariable=balance_var2017)
        balance_2017.grid(column=6, row=self.row + 4, padx=5, pady=5)

        balance_zloty_2017 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_2017.grid(column=7, row=self.row + 4)

        balance_zloty_thousands_2017 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_thousands_2017.grid(column=8, row=self.row + 4)

        balance_zloty_thousands_rounded_2017 = Label(self.scrollable_frame, text='0.00', fg=LABEL_COLOR, font=LABEL_FONT)
        balance_zloty_thousands_rounded_2017.grid(column=9, row=self.row + 4)

        employment_2017 = Entry(self.scrollable_frame, width=20).grid(column=10, row=self.row + 4, padx=5, pady=5)

        def update_income_labels(s_var, income_zloty_input,
                                 income_zloty_thousand_input, income_zloty_thousand_rounded_input, actual_euro_rate):
            """Updates income labels with euro rate calculates"""
            if s_var.get():
                income_in_euro = round(float(s_var.get().replace(',', '.')) / actual_euro_rate, 2)
            else:
                income_in_euro = 0.00

            income_zloty_input.config(text=income_in_euro)
            income_zloty_thousand_input.config(text=income_in_euro / 1000)
            income_zloty_thousand_rounded_input.config(text=round(income_in_euro / 1000, 2))

            # Update result
            self.result['2020']['Przychody'] = float(s_var.get()) # zamiast roku stałą year przekazana do funkcji
            self.result_income_2020.config(text=self.result['2020']['Przychody'])#????????????????????????????????

        def update_balance_labels(s_var, balance_zloty_input,
                                  balance_zloty_thousand_input, balance_zloty_thousand_rounded_input, actual_euro_rate):
            """Updates balance labels with euro rate calculates"""
            if s_var.get():
                balance_in_euro = round(float(s_var.get().replace(',', '.')) / actual_euro_rate, 2)
            else:
                balance_in_euro = 0.00

            balance_zloty_input.config(text=balance_in_euro)
            balance_zloty_thousand_input.config(text=balance_in_euro / 1000)
            balance_zloty_thousand_rounded_input.config(text=round(balance_in_euro / 1000, 2))

        def update_employment_status(s_var):
            print(s_var.get())

    def set_result_table(self):

        bottom_canvas = Canvas(self.container, width=1450, height=150)
        bottom_canvas.config(bg=RESULT_COLOR)
        bottom_canvas.grid(sticky='ew')

        result_year_2020_label = Label(bottom_canvas, text='2020', fg='white', bg=RESULT_COLOR, font=LABEL_FONT) \
            .grid(column=0, row=1, padx=5, pady=5)

        result_year_2019_label = Label(bottom_canvas, text='2019', fg='white', bg=RESULT_COLOR, font=LABEL_FONT) \
            .grid(column=0, row=2, padx=5, pady=5)

        result_year_2018_label = Label(bottom_canvas, text='2018', fg='white', bg=RESULT_COLOR, font=LABEL_FONT) \
            .grid(column=0, row=3, padx=5, pady=5)

        result_year_2017_label = Label(bottom_canvas, text='2017', fg='white', bg=RESULT_COLOR, font=LABEL_FONT) \
            .grid(column=0, row=4, padx=5, pady=5)

        result_euro_rate = Label(bottom_canvas, text='Kurs Euro', fg='white', bg=RESULT_COLOR, font=LABEL_FONT) \
            .grid(column=1, row=0, padx=5, pady=5)

        result_income = Label(bottom_canvas, text='Przychody', fg='white', bg=RESULT_COLOR, font=LABEL_FONT) \
            .grid(column=2, row=0, padx=5, pady=5)

        result_income_zloty = Label(bottom_canvas, text='Przychody zloty', fg='white', bg=RESULT_COLOR, font=LABEL_FONT) \
            .grid(column=3, row=0, padx=5, pady=5)

        result_income_zloty_thousand = Label(bottom_canvas, text='Przychody zloty (tys.)',
                                      font=LABEL_FONT, fg='white', bg=RESULT_COLOR, padx=15).grid(column=4, row=0, padx=5, pady=5)

        result_income_zloty_thousand_rounded = Label(bottom_canvas, text='Przychody zloty (tys. zaokr.)', fg='white', bg=RESULT_COLOR,
                                              font=LABEL_FONT).grid(column=5, row=0, padx=5, pady=5)

        result_balance = Label(bottom_canvas, text='Bilans', fg='white', bg=RESULT_COLOR, font=LABEL_FONT) \
            .grid(column=6, row=0, padx=5, pady=5)

        result_balance_zloty = Label(bottom_canvas, text='Bilans zloty', fg='white', bg=RESULT_COLOR, font=LABEL_FONT) \
            .grid(column=7, row=0, padx=5, pady=5)

        result_balance_zloty_thousands = Label(bottom_canvas, text='Bilans zloty (tys.)', fg='white', bg=RESULT_COLOR, font=LABEL_FONT)\
            .grid(column=8, row=0, padx=5, pady=5)

        result_balance_zloty_thousands_rounded = Label(bottom_canvas, text='Bilans zloty (tys. zaokr.)', fg='white', bg=RESULT_COLOR, font=LABEL_FONT)\
            .grid(column=9, row=0, padx=5, pady=5)

        result_employment = Label(bottom_canvas, text='Zatrudnienie', bg=RESULT_COLOR, fg='white', font=LABEL_FONT) \
            .grid(column=10, row=0, padx=5, pady=5)

        euro_rate_2020 = Label(bottom_canvas, text=EURO_RATE_2020, bg=RESULT_COLOR, fg=LABEL_COLOR, font=LABEL_FONT)
        euro_rate_2020.grid(column=1, row=1, padx=5)

        euro_rate_2019 = Label(bottom_canvas, text=EURO_RATE_2019, bg=RESULT_COLOR, fg=LABEL_COLOR, font=LABEL_FONT)
        euro_rate_2019.grid(column=1, row=2, padx=5)

        euro_rate_2018 = Label(bottom_canvas, text=EURO_RATE_2018, bg=RESULT_COLOR, fg=LABEL_COLOR, font=LABEL_FONT)
        euro_rate_2018.grid(column=1, row=3, padx=5)

        euro_rate_2017 = Label(bottom_canvas, text='4,1709', bg=RESULT_COLOR, fg=LABEL_COLOR, font=LABEL_FONT)
        euro_rate_2017.grid(column=1, row=4, padx=5)

        # 2020

        self.result_income_2020 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2020.grid(column=2, row=1, padx=5, pady=5)

        self.result_income_2020_zloty = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2020_zloty.grid(column=3, row=1, padx=5, pady=5)

        self.result_income_2020_zloty_thousand = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2020_zloty_thousand.grid(column=4, row=1, padx=5, pady=5)

        self.result_income_2020_zloty_thousand_rounded = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2020_zloty_thousand_rounded.grid(column=5, row=1, padx=5, pady=5)

        self.result_balance_2020 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_2020.grid(column=6, row=1, padx=5, pady=5)

        self.result_balance_zloty_2020 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_zloty_2020.grid(column=7, row=1, padx=5, pady=5)

        self.result_balance_zloty_thousands_2020 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_zloty_thousands_2020.grid(column=8, row=1, padx=5, pady=5)

        self.result_balance_zloty_thousands_rounded_2020 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_zloty_thousands_rounded_2020.grid(column=9, row=1, padx=5, pady=5)

        self.result_employment_2020 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_employment_2020.grid(column=10, row=1, padx=5, pady=5)

        # 2019

        self.result_income_2019 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2019.grid(column=2, row=2, padx=5, pady=5)

        self.result_income_2019_zloty = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2019_zloty.grid(column=3, row=2, padx=5, pady=5)

        self.result_income_2019_zloty_thousand = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2019_zloty_thousand.grid(column=4, row=2, padx=5, pady=5)

        self.result_income_2019_zloty_thousand_rounded = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR,
                                                               font=LABEL_FONT)
        self.result_income_2019_zloty_thousand_rounded.grid(column=5, row=2, padx=5, pady=5)

        self.result_balance_2019 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_2019.grid(column=6, row=2, padx=5, pady=5)

        self.result_balance_zloty_2019 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_zloty_2019.grid(column=7, row=2, padx=5, pady=5)

        self.result_balance_zloty_thousands_2019 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_zloty_thousands_2019.grid(column=8, row=2, padx=5, pady=5)

        self.result_balance_zloty_thousands_rounded_2019 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR,
                                                                 font=LABEL_FONT)
        self.result_balance_zloty_thousands_rounded_2019.grid(column=9, row=2, padx=5, pady=5)

        self.result_employment_2019 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_employment_2019.grid(column=10, row=2, padx=5, pady=5)

        # 2018

        self.result_income_2018 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2018.grid(column=2, row=3, padx=5, pady=5)

        self.result_income_2018_zloty = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2018_zloty.grid(column=3, row=3, padx=5, pady=5)

        self.result_income_2018_zloty_thousand = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2018_zloty_thousand.grid(column=4, row=3, padx=5, pady=5)

        self.result_income_2018_zloty_thousand_rounded = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR,
                                                               font=LABEL_FONT)
        self.result_income_2018_zloty_thousand_rounded.grid(column=5, row=3, padx=5, pady=5)

        self.result_balance_2018 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_2018.grid(column=6, row=3, padx=5, pady=5)

        self.result_balance_zloty_2018 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_zloty_2018.grid(column=7, row=3, padx=5, pady=5)

        self.result_balance_zloty_thousands_2018 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_zloty_thousands_2018.grid(column=8, row=3, padx=5, pady=5)

        self.result_balance_zloty_thousands_rounded_2018 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR,
                                                                 font=LABEL_FONT)
        self.result_balance_zloty_thousands_rounded_2018.grid(column=9, row=3, padx=5, pady=5)

        self.result_employment_2018 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_employment_2018.grid(column=10, row=3, padx=5, pady=5)

        # 2017

        self.result_income_2017 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2017.grid(column=2, row=4, padx=5, pady=5)

        self.result_income_2017_zloty = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2017_zloty.grid(column=3, row=4, padx=5, pady=5)

        self.result_income_2017_zloty_thousand = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_income_2017_zloty_thousand.grid(column=4, row=4, padx=5, pady=5)

        self.result_income_2017_zloty_thousand_rounded = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR,
                                                               font=LABEL_FONT)
        self.result_income_2017_zloty_thousand_rounded.grid(column=5, row=4, padx=5, pady=5)

        self.result_balance_2017 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_2017.grid(column=6, row=4, padx=5, pady=5)

        self.result_balance_zloty_2017 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_zloty_2017.grid(column=7, row=4, padx=5, pady=5)

        self.result_balance_zloty_thousands_2017 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_balance_zloty_thousands_2017.grid(column=8, row=4, padx=5, pady=5)

        self.result_balance_zloty_thousands_rounded_2017 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR,
                                                                 font=LABEL_FONT)
        self.result_balance_zloty_thousands_rounded_2017.grid(column=9, row=4, padx=5, pady=5)

        self.result_employment_2017 = Label(bottom_canvas, text='0.00', bg=RESULT_COLOR, font=LABEL_FONT)
        self.result_employment_2017.grid(column=10, row=4, padx=5, pady=5)
