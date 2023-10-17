import tkinter
import tkinter.messagebox


class GradeAverage:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x350')

        self.main_window.configure(bg='green')

        self.top_frame = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.test1 = tkinter.Label(self.top_frame, text='Enter the score for test 1:', bg='green', font='Helvetica', fg='yellow')
        self.test1_entry = tkinter.Entry(self.top_frame, width=10, bg='green', font='Helvetica', fg='yellow')

        self.test2 = tkinter.Label(self.frame2, text='Enter the score for test 2:', bg='green', font='Helvetica', fg='yellow')
        self.test2_entry = tkinter.Entry(self.frame2, width=10, bg='green', font='Helvetica', fg='yellow')

        self.test3 = tkinter.Label(self.frame3, text='Enter the score for test 3:', bg='green', font='Helvetica', fg='yellow')
        self.test3_entry = tkinter.Entry(self.frame3, width=10, bg='green', font='Helvetica', fg='yellow')

        self.test1.pack(side='left')
        self.test1_entry.pack(side='left')

        self.test2.pack(side='left')
        self.test2_entry.pack(side='left')
        
        self.test3.pack(side='left')
        self.test3_entry.pack(side='left')

        self.score_var = tkinter.StringVar()

        self.score_var.set('0.00')

        self.average_label = tkinter.Label(self.frame4, text='Average:', bg='green', font='Helvetica', fg='yellow')

        self.score_label = tkinter.Label(self.frame4, textvariable=self.score_var, bg='green', font='Helvetica', fg='yellow')

        self.average_label.pack(side='left')
        self.score_label.pack(side='left')

        self.avg_button = tkinter.Button(self.bottom_frame, text='Average',command=self.average, bg='green', font='Helvetica', fg='yellow')
        self.quitbutton = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy, bg='green', font='Helvetica', fg='yellow')

        self.avg_button.pack(side='left')
        self.quitbutton.pack(side='left')

        self.top_frame.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def average(self):
        score1 = float(self.test1_entry.get())
        score2 = float(self.test2_entry.get())
        score3 = float(self.test3_entry.get())

        average_score = round((score1 + score2 + score3)/3, 2)

        self.score_var.set(average_score)

gradeaverage = GradeAverage()