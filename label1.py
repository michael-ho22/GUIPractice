import tkinter

class MyGUI:
    def __init__(self):
        #created 3 attributes: main_window, label1, label2
        self.main_window = tkinter.Tk()

        # configure the main window
        self.main_window.geometry('500x200') #controls size of window
        self.main_window.title('Label Demo')



        self.label1 = tkinter.Label(self.main_window, text = 'Hello World!')
        self.label2 = tkinter.Label(self.main_window, text = 'This is my GUI program.')

        self.label1.pack(side='left') # it makes widgets actually appear on main window
        self.label2.pack(side='right')

        tkinter.mainloop() #essentially allows the GUI to keep running until you're done (keeps looping)

#create an instance of the MyGUI class
my_gui = MyGUI()


print('moving on.....')
