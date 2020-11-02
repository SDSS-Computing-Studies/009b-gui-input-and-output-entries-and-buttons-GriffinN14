"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
import tkinter as tk
from tkinter import *
window = tk.Tk()


aoutput = StringVar()
aoutput.set("Name")

boutput = StringVar()
boutput.set("Theme")

coutput = StringVar()
coutput.set("A Place")

doutput = StringVar()
doutput.set("Day of the week")

eoutput = StringVar()
eoutput.set("Time")

foutput = StringVar()
foutput.set("Verb")

goutput = StringVar()
goutput.set("Animal")

houtput = StringVar()
houtput.set("Body part")

ioutput = StringVar()
ioutput.set("Contact information")

def button_pressed():
    a = aoutput.get()
    b = boutput.get()
    c = coutput.get()
    d = doutput.get()
    e = eoutput.get()
    f = foutput.get()
    g = goutput.get()
    h = houtput.get()
    i = ioutput.get()

    madlib=( a + " is having a\n" + b + " party!\nit's going to be at " + c + "\non " + d + ".\nPlease make sure to show up at\n" + e + ", or else\nYou will be required to\n" + f + " a " + g + "\nwith your " + h + ".\nRSVP at " + i + ".")
    ml = StringVar()
    ml.set(madlib)
    mllabel = tk.Label(window, textvar=ml)
    mllabel.pack()

button1 = tk.Button(window, text="Enter", command=button_pressed )

a_entry = Entry(window, width=20, textvariable=aoutput)
a_entry.pack()
b_entry = Entry(window, width=20, textvariable=boutput)
b_entry.pack()
c_entry = Entry(window, width=20, textvariable=coutput)
c_entry.pack()
d_entry = Entry(window, width=20, textvariable=doutput)
d_entry.pack()
e_entry = Entry(window, width=20, textvariable=eoutput)
e_entry.pack()
f_entry = Entry(window, width=20, textvariable=foutput)
f_entry.pack()
g_entry = Entry(window, width=20, textvariable=goutput)
g_entry.pack()
h_entry = Entry(window, width=20, textvariable=houtput)
h_entry.pack()
i_entry = Entry(window, width=20, textvariable=ioutput)
i_entry.pack()
button1.pack()


window.mainloop()