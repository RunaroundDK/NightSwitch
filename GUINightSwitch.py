from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import subprocess

window = Tk()
window.title('Night Switch')
window.geometry('340x150')

mylabel = Label(window, text = '    Select how long you will be gone for...', font = ("Purisa", 12)) # window can be a window or a frame
mylabel.grid() # packs the label on to the window

selected = IntVar()

hour1 = Radiobutton(window,text='1 hour', value=1, variable=selected)
hour2 = Radiobutton(window,text='2 hour', value=2, variable=selected)
hour3 = Radiobutton(window,text='3 hour', value=3, variable=selected)

def clicked():
   #print(selected.get()) # prints onto the terminal
   messagebox.showwarning('ALERT', 'Your Computer will Shutdown in ' + str(selected.get()) + ' hours') # Converting the int into a string
   # Add the system command here when clicked
   subprocess.Popen('sleep %sm && shutdown' % (selected.get()), shell=True)


btn = Button(window, text='Select One', command=clicked) # When Button is clicked direct towards the clicked function

hour1.grid(column=0, row=1)
hour2.grid(column=0, row=2)
hour3.grid(column=0, row=3)
btn.grid(column=0, row=4)


window.mainloop()
