import time
import random
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Calculator")

wind_width = 515
wind_height = 535
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord  = (screen_width/2)-(wind_width/2)
y_coord  = (screen_height/2)-(wind_height/2)
root.geometry("%dx%d+%d+%d" % (wind_width, wind_height, x_coord, y_coord))

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_columnconfigure(2, weight = 1)
root.grid_columnconfigure(3, weight = 1)
root.grid_rowconfigure(0, weight = 2)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)
root.grid_rowconfigure(3, weight = 1)
root.grid_rowconfigure(4, weight = 1)
root.grid_rowconfigure(5, weight = 1)

result = "              "

button_fill = "WENS"

button_height = 1
button_width = 3
button_bg = "#1D191C"
button_fg = "#F8EFF1"
screen_bg = "#1D191C"
root_colour = "#1D191C"
grid_font = "Verdana 20 bold"
top_font = "Verdana 12 bold"
score_font = "Verdana 20 bold"

root.configure(bg = root_colour)


screen = Label(root, text = result, bd = 4, relief = "sunken", fg = button_fg, bg = screen_bg, font = score_font, padx = 12, pady = 5)
screen.grid(row = 0, column = 0, columnspan = 4, sticky= button_fill)


def Add_to(input):
    global result
    result += input
    screen.configure(text = result)


def Clear():
    global result
    result = ""
    screen.configure(text = result)


def Backspace():
    global result
    result = result[:-1]
    screen.configure(text = result)


def Equals():
    global result
    try:
        result = str(eval(result))
    except:
        pass
    screen.configure(text = result)


clear = Button(root, text= "Clear", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Clear())
clear.grid(row = 1, column = 0, sticky= button_fill)
clear.bind("<Button-1>")

backspace = Button(root, text= "Backspace", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Backspace())
backspace.grid(row = 1, column = 1, columnspan = 2, sticky= button_fill)
backspace.bind("<Button-1>")

point = Button(root, text= ".", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("."))
point.grid(row = 5, column = 2, sticky= button_fill)
point.bind("<Button-1>")


button0 = Button(root, text= "0", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("0"))
button0.grid(row = 5, column = 0, columnspan = 2, sticky= button_fill)
button0.bind("<Button-1>")

button1 = Button(root, text= "1", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("1"))
button1.grid(row = 4, column = 0, sticky= button_fill)
button1.bind("<Button-1>")

button2 = Button(root, text= "2", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("2"))
button2.grid(row = 4, column = 1, sticky= button_fill)
button2.bind("<Button-1>")

button3 = Button(root, text= "3", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("3"))
button3.grid(row = 4, column = 2, sticky= button_fill)
button3.bind("<Button-1>")

button4 = Button(root, text= "4", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("4"))
button4.grid(row = 3, column = 0, sticky= button_fill)
button4.bind("<Button-1>")

button5 = Button(root, text= "5", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("5"))
button5.grid(row = 3, column = 1, sticky= button_fill)
button5.bind("<Button-1>")

button6 = Button(root, text= "6", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("6"))
button6.grid(row = 3, column = 2, sticky= button_fill)
button6.bind("<Button-1>")

button7 = Button(root, text= "7", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("7"))
button7.grid(row = 2, column = 0, sticky= button_fill)
button7.bind("<Button-1>")

button8 = Button(root, text= "8", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("8"))
button8.grid(row = 2, column = 1, sticky= button_fill)
button8.bind("<Button-1>")

button9 = Button(root, text= "9", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("9"))
button9.grid(row = 2, column = 2, sticky= button_fill)
button9.bind("<Button-1>")

division = Button(root, text= "÷", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("/"))
division.grid(row = 1, column = 3, sticky= button_fill)
division.bind("<Button-1>")

multi = Button(root, text= "x", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("*"))
multi.grid(row = 2, column = 3, sticky= button_fill)
multi.bind("<Button-1>")

minus = Button(root, text= "-", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("-"))
minus.grid(row = 3, column = 3, sticky= button_fill)
minus.bind("<Button-1>")

plus = Button(root, text= "+", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Add_to("+"))
plus.grid(row = 4, column = 3, sticky= button_fill)
plus.bind("<Button-1>")

equals = Button(root, text= "=", fg = button_fg, bg = button_bg, font = grid_font, height = button_height, width = button_width, command = lambda: Equals())
equals.grid(row = 5, column = 3, sticky= button_fill)
equals.bind("<Button-1>")


all_widgets = (button1, button2, button3, button4, button5, button6, button7, button8, button9, screen)


root.mainloop()
