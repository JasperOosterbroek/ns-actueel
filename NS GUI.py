from tkinter import *

root = Tk()
mainPage = Frame(root)
root.resizable(False, False)
root.configure(height=100)
png = PhotoImage(file="NS2.png")
x = Label(image = png)
x.grid(row=0, column=0)
x.lower()

buttonframe = Frame(root, background="#feca24")
buttonframe.grid(row=0,column=0,columnspan=1, )
Button(buttonframe, text='Ik wil naar \nAmsterdam', background='#493782', foreground="#fff", height=3, width=10, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=0, padx=20,)
Button(buttonframe, text='Ik wil naar \nAmsterdam', background='#493782', foreground="#fff", height=3, width=10, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=1, padx=20)
Button(buttonframe, text='Ik wil naar \nAmsterdam', background='#493782', foreground="#fff", height=3, width=10, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=2, padx=20)
Button(buttonframe, text='Ik wil naar \nAmsterdam', background='#493782', foreground="#fff", height=3, width=10, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=3, padx=20)



root.mainloop()