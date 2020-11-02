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
window = tk.Tk()

bv = StringVar()
bv.set("B")
cv = StringVar()
cv.set("C")

instuct = tk.Label(window, text="Enter b and c and the program will factor them")
b = tk.Entry(window, textvar=bv)
c = tk.Entry(window, textvar=cv)

instuct.grid(row=1,column=1,columnspan=2)
b.grid(row=2,column=1)
c.grid(row=2,column=2)

window.mainloop()