from tkinter import *
class gui:
    '''The gui system
    '''

    def __init__(self,master):
        '''Return a gui object wich is used for all things gui '''
        self.master = master
        self.master.resizable(False, False)

        self.homepng = PhotoImage(file="NS.png")
        self.cleanpng = PhotoImage(file="NSClean.png")
        self.gobackpng = PhotoImage(file="home.png")

        self.background = Label(image = self.homepng)
        self.background.grid(row=0, column=0)
        # all frames here please
        self.homepageframe = Frame(self.master, background="#feca24")




        # build first page
        self.buildhomepage()

    def clearframe(self,frame):
        '''clear/'s specified frame'''
        print(frame.grid_info())
        for widget in frame.winfo_children():
            widget.pack_forget()
            widget.grid_forget()
        frame.destroy()

    def  changeframe(self,currentframe,newframe):
        '''Change to desired frame'''
        self.clearframe(currentframe)
        if(newframe == 'testpage'):
            self.testframe= Frame(self.master,background="#feca24")
            self.buildtestpage()
        elif(newframe == 'homepage'):
            self.homepageframe = Frame(self.master,background="#feca24")
            self.buildhomepage()
            self.clearframe(self.gohomeframe)
        elif(newframe =='goto'):
            self.gotoframe = Frame(self.master, background="#feca24")
            self.buildgoto()



    def buildhomepage(self):
        self.homepageframe.grid(row=0, column=0, columnspan=1, )
        self.background.config(image=self.homepng)
        Button(self.homepageframe, text='Ik wil naar \nAmsterdam', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic'), command=lambda: self.changeframe(self.homepageframe, 'goto')).grid(row=0, column=0, padx=20, )
        Button(self.homepageframe, text='Kopen \n los kaartje', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic')).grid(row=0, column=1, padx=20)
        Button(self.homepageframe, text='Kopen \n OV-Chipkaart', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic')).grid(row=0, column=2, padx=20)
        Button(self.homepageframe, text='Ik wil naar \nhet buitenland', background='#493782', foreground="#fff", height=3,
               width=12, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=3, padx=20)
        Button(self.homepageframe, text='Reisinformatie \nopvragen', background='#493782', foreground="#fff", height=3,
               width=12, font=('Helvetica', 10, 'bold italic'),command =lambda: self.changeframe(self.homepageframe,'testpage')).grid(row=0, column=4, padx=20)
        self.homepageframe.place(y=400, x=35)

    def buildtestpage(self):
        self.buildgohome(self.testframe)
        self.background.config(image=self.cleanpng)
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


    def buildgoto(self):
        self.buildgohome(self.gotoframe)
        self.background.config(image = self.cleanpng)
        Label(self.gotoframe, text="De reis naar Amsterdam kost €10", background="#2c2c2c").grid(row=0, column=0, padx=20, )
        self.gotoframe.place(y=200, x=270)


    def buildgohome(self,currentframe):
        self.gohomeframe = Frame(self.master, background="#00236a")
        self.gohomeframe.grid(row=0, column=0, columnspan=1, )
        Button(self.gohomeframe, image = self.gobackpng, height=34, width=34, borderwidth=0, cursor="man", command=lambda: self.changeframe(currentframe, 'homepage')).grid(row=0, column=0, padx=20, )
        self.gohomeframe.place(y=550, x=40)

root = Tk()
gui = gui(root)
root.mainloop()
