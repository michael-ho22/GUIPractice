import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        self.radio_var = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 1',
                                       variable=self.radio_var,
                                       value=1,
                                       command=self.show_choice)
        
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 2',
                                       variable=self.radio_var,
                                       value=2)
        
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 3',
                                       variable=self.radio_var,
                                       value=3)
        
        # self.radio_var.set(2)
        
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        
        self.reset_button = tkinter.Button(self.bottom_frame,
                                           text='Reset',
                                           command=self.reset_radio_button)
        
        self.destroy_button = tkinter.Button(self.bottom_frame,
                                        text='Quit',
                                        command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.reset_button.pack(side='left')
        self.destroy_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo('Selection', 'You have selected option' + str(self.radio_var.get()))

    def reset_radio_button(self):
        self.radio_var.set(1)

my_gui = MyGUI()