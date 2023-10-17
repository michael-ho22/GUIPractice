import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #created 3 attributes: main_window, label1, label2
        self.main_window = tkinter.Tk()

        # configure the main window
        self.main_window.geometry('500x200') #controls size of window
        self.main_window.title('Label Demo')


        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        self.label1 = tkinter.Label(self.top_frame, text = 'John') #makes frames within main window
        self.label2 = tkinter.Label(self.top_frame, text = 'James')
        self.label3 = tkinter.Label(self.top_frame, text = 'Jack')

        self.label1.pack(side='left') # it makes widgets actually appear on main window (only for top frame)
        self.label2.pack(side='left')
        self.label3.pack(side='left')

        self.label4 = tkinter.Label(self.bottom_frame, text = 'Jane')
        self.label5 = tkinter.Label(self.bottom_frame, text = 'Jill')
        self.label6 = tkinter.Label(self.bottom_frame, text = 'Jamie')

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        #has three arguments, but creates a button within main window 
        self.mybutton = tkinter.Button(self.main_window, text = 'Click Me!', command = self.do_something) #this button does something when you click
        self.quitbutton = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy) #this button closes entire window

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.mybutton.pack(side='left')
        self.quitbutton.pack(side='right')

        tkinter.mainloop() #essentially allows the GUI to keep running until you're done (keeps looping)

    def do_something(self): #defines do_something method
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button!')

#create an instance of the MyGUI class
my_gui = MyGUI()


print('moving on.....')