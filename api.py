import requests as req
import xmltodict
from tkinter import *


def requestStationData(station):
    r = req.get('http://webservices.ns.nl/ns-api-avt?station=' + station, auth=('jasper.oosterbroek@student.hu.nl', 'JXwCrdq5iel_il2lLgaWhq-3AtpqZ-2r1s_UC0CLIc72XN9G7aM5vg'))
    if r.status_code == 200:
        nicetext = xmltodict.parse(r.text)
        return nicetext
    else:
        return 'error'


#  tijdelijke code voor het wisselen van schermen
def raise_frame(frame):
    frame.tkraise()

root = Tk()

f1 = Frame(root)
f2 = Frame(root)


for frame in (f1, f2,):
    frame.grid(row=0, column=0, sticky='news')

Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
Label(f1, text='FRAME 1').pack()

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()