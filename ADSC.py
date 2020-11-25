from Tkinter import *
import tkMessageBox
from PIL import ImageTk, Image
import os


#defining different types of elements on TK as an object
class button(object):
    def __init__(self,frame,name,row,column,width,height,bg,fg,command=None,text=None,state=DISABLED):
        self.name = name
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.bg = bg
        self.fg = fg
        self.command = command
        self.text = text
        self.state = state
        self.name = Button(
            frame,
            width = self.width,
            height = self.height,
            text = self.text,
            bg = bg,
            fg = fg,
            command = self.command,
            state = self.state)
        self.name.grid(
            row = self.row,
            column = self.column,
            sticky = 'NESW',
            padx = 2,
            pady = 2)

class label(object):
    def __init__(self,frame,name,row,column,bg,fg,img,font,font_color):
        self.name = name
        self.row = row
        self.column = column
        self.bg = bg
        self.fg = fg
        self.img = img
        self.font = font
        self.fg = font_color
        self.name = Label(
            frame,
            text = name,
            image = img)
        self.name.config(
            font = self.font,
            bg = self.bg,
            fg = self.fg,
            justify = 'center',
            borderwidth = 3)
        self.name.grid(
            row=self.row,
            column=self.column,
            sticky='NESW',
            padx=1,
            pady=1)

class entry(object):
    def __init__(self,frame,row,column,text_variable = None, state = NORMAL):
        self.row = row
        self.column = column
        self.text_variable = text_variable
        self.state = state
        self.name = Entry(frame)
        self.name.focus()
        self.name.config(
            font=("Helvetica 12"),
            justify='center',
            borderwidth=2,
            textvariable = self.text_variable,
            state = self.state)
        self.name.grid(
            row=self.row,
            column=self.column,
            sticky='NESW',
            padx=1,
            pady=5)
    def get(self):
        return self.name.get()

class checkbutton(object):
    def __init__(self,frame,row,column,bg,activefg,text,state,variable):
        self.row = row
        self.column = column
        self.bg = bg
        self.text = text
        self.state = state
        self.activefg = activefg
        self.variable = variable
        self.name = Checkbutton(
            frame,
            variable = variable,
            onvalue = 1,
            offvalue = 0)
        self.name.config(
            font=("Helvetica 12"),
            justify='center',
            bg = self.bg,
            borderwidth = 2,
            text = self.text,
            state = self.state,
            activeforeground = self.activefg)
        self.name.grid(
            row=self.row,
            column=self.column,
            sticky='NESW',
            padx=1,
            pady=5)


#creating the main window
main_window = Tk()
main_window.title("ADSC")
main_window.geometry('1920x1080')
main_window.config(bg = 'black')


if __name__ == "__main__":
    main_window.mainloop()
    