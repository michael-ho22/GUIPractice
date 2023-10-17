import tkinter
import tkinter.messagebox


class KiloConverterGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.main_window.geometry('250x100')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.promt_label = tkinter.Label(self.top_frame, text='Enter a distance in Kilometer:')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.promt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Converter',command=self.convert)
        self.quitbutton = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quitbutton.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round(kilo * 0.6214, 2)

        #convert kilo into string as the messagebox only displays string
        tkinter.messagebox.showinfo('Results', str(kilo) + ' kilometers is equal to ' + str(miles) + ' miles')

kilo_convert = KiloConverterGUI()