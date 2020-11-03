"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk
from tkinter import *
import random
from random import randint
window = tk.Tk()

bv = StringVar()
bv.set("B")
cv = StringVar()
cv.set("C")
factors = StringVar()

def factor():
    ba = int(b.get())
    ca = int(c.get())
    worked = 1
    for i in range(1000):
        r = randint(1,15)
        r2 = randint(1,15)
        if r + r2 == ba and r*r2 == ca:
            worked = worked + 1
            if r > r2:
                fac=("(x + " + str(r2) + ")(x + " + str(r) + ")")
                factors.set(fac)
            else:
                fac=("(x + " + str(r) + ")(x + " + str(r2) + ")")
                factors.set(fac)
    if worked == 1:
        fac=("cannot be factored")
        factors.set(fac)


instuct = tk.Label(window, text="Enter b and c and the program will factor them")
b = tk.Entry(window, textvar=bv)
c = tk.Entry(window, textvar=cv)
button = tk.Button(window, text="  =  ",command=factor)

instuct.grid(row=1,column=1,columnspan=2)
b.grid(row=2,column=1)
c.grid(row=2,column=2)
button.grid(row=3,column=1,columnspan=2)
answer = tk.Entry(window, textvariable=factors)
answer.grid(row=4,column=1,columnspan=2)

window.mainloop()