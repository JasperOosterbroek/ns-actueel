from tkinter import *
class gui:
    '''The gui system
    '''

    def __init__(self,master):
        '''Return a gui object wich is used for all things gui '''
        self.master = master
        self.master.resizable(False, False)
        self.png = PhotoImage(file="NS.png")
        self.background = Label(image = self.png)
        self.background.grid(row=0, column=0)
        # all frames here please
        self.buttonframe = Frame(self.master, background="#feca24")
        self.testframe = Frame(self.master, background="#feca24")

        # build first page
        self.buildhomepage()

    def clearframe(self,frame):
        '''clear/'s specified frame'''
        print(frame.grid_info())
        for widget in frame.winfo_children():
            widget.pack_forget()
            widget.grid_forget()

    def  changeframe(self,currentframe,newframe):
        '''Change to desired frame'''
        self.clearframe(currentframe)
        if(newframe == 'testpage'):
            self.buildtestpage()
        elif(newframe == 'homepage'):
            self.buildhomepage()


    def buildhomepage(self):
        self.buttonframe.grid(row=0, column=0, columnspan=1, )
        Button(self.buttonframe, text='Ik wil naar \nAmsterdam', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic')).grid(row=0, column=0, padx=20, )
        Button(self.buttonframe, text='Kopen \n los kaartje', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic')).grid(row=0, column=1, padx=20)
        Button(self.buttonframe, text='Kopen \n OV-Chipkaart', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic')).grid(row=0, column=2, padx=20)
        Button(self.buttonframe, text='Ik wil naar \nhet buitenland', background='#493782', foreground="#fff", height=3,
               width=12, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=3, padx=20)
        Button(self.buttonframe, text='Reisinformatie \nopvragen', background='#493782', foreground="#fff", height=3,
               width=12, font=('Helvetica', 10, 'bold italic'),command =lambda: self.changeframe(self.buttonframe,'testpage')).grid(row=0, column=4, padx=20)
        self.buttonframe.place(y=400, x=35)

    def buildtestpage(self):
        self.testframe.grid(row=0, column=0, columnspan=1, )
        Button(self.testframe, text='kak', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic')).grid(row=0, column=0, padx=20, )
        Button(self.testframe, text='kak', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic')).grid(row=0, column=1, padx=20)
        Button(self.testframe, text='kak', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic')).grid(row=0, column=2, padx=20)
        Button(self.testframe, text='kak', background='#493782', foreground="#fff", height=3,
               width=12, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=3, padx=20)
        Button(self.testframe, text='kak', background='#493782', foreground="#fff", height=3,
               width=12, font=('Helvetica', 10, 'bold italic'),command =lambda: self.clearframe(self.testframe)).grid(row=0, column=4, padx=20)
        self.testframe.place(y=400, x=35)




root = Tk()
gui = gui(root)
root.mainloop()
