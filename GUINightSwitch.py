from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import subprocess

#Creates Box
window = Tk()
window.title('Night Switch')
window.geometry('340x150')

#Prints to screen
mylabel = Label(window, text = '    Select how long you will be gone for...', font = ("Purisa", 12)) # window can be a window or a frame
mylabel.grid() # packs the label on to the window

selected = IntVar()

#Gives buttons
hour1 = Radiobutton(window, text='1 hour', value=1, variable=selected)
hour2 = Radiobutton(window, text='2 hour', value=2, variable=selected)
hour3 = Radiobutton(window, text='3 hour', value=3, variable=selected)

#When button clicked do this
def clicked():
   #print(selected.get()) # prints onto the terminal
   messagebox.showwarning('ALERT', 'Your Computer will Shutdown in ' + str(selected.get()) + ' hours') # Converting the int into a string
   # Add the system command here when clicked
   subprocess.Popen('sleep %sh && shutdown' % (selected.get()), shell=True) #Switched From 1 Min to 1 hour
   print('Your computer will now shutdown in ' + str(selected.get()) + 'hours, please do not close terminal') # prints message onto termianl

#When close button clicked, close box
def closeBox():
    window.destroy() #Destroys the main window

#The buttons
btn = Button(window, text='Select One', command=clicked) # When Button is clicked direct towards the clicked function
btn1 = Button(window, text='close window', command=closeBox) #Closes the window after

#Girds and location of buttons
hour1.grid(column=0, row=1)
hour2.grid(column=0, row=2)
hour3.grid(column=0, row=3)
btn.grid(column=0, row=4)
btn1.grid(column=0, row=5)


window.mainloop()
