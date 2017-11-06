from tkinter import *

root = Tk()

root.resizable(False, False)
png = PhotoImage(file="NS.png")
background = Label(image = png)
background.grid(row=0, column=0)

buttonframe = Frame(root, background="#feca24")
buttonframe.grid(row=0,column=0,columnspan=1, )
Button(buttonframe, text='Ik wil naar \nAmsterdam',     background='#493782', foreground="#fff", height=3, width=12, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=0, padx=20,)
Button(buttonframe, text='Kopen \n los kaartje',        background='#493782', foreground="#fff", height=3, width=12, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=1, padx=20)
Button(buttonframe, text='Kopen \n OV-Chipkaart',       background='#493782', foreground="#fff", height=3, width=12, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=2, padx=20)
Button(buttonframe, text='Ik wil naar \nhet buitenland',background='#493782', foreground="#fff", height=3, width=12, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=3, padx=20)
Button(buttonframe, text='Reisinformatie \nopvragen',   background='#493782', foreground="#fff", height=3, width=12, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=4, padx=20)
buttonframe.place(y=400, x=35)  # !!!


root.mainloop()