

from tkinter import *
import tkinter.messagebox
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkvideo import tkvideo




#creating a tk parent GUI
master = Tk()
master.title("My Window")
master.geometry("600x400")


#adding button to the frame
quit = Button (master,text="Click on",command=master.destroy)
quit.pack()


#using place geometry
quit2 = Button(master,text = "click on again", command=master.destroy)
quit2.place(height = 100 , width= 100)
quit2.pack()


# call back function
def quit3 ():
    print("Hello, getting out of here")
    master.destroy()
    
widget = Button(master, text = "press me to quit",command= quit)
widget.pack()
#label    
var = StringVar()
label = Label (master, textvariable = var, relief = RAISED)

var.set("This is a Python class")
label.pack()    

#Change label Content

def change_text():
    new_text = "This is Changed text!!"
    var.set(new_text)
    
var = StringVar()
label = Label(master, textvariable= var, relief = RAISED)
var.set("This is a TEST")
label.pack()
button = Button(master, text = "Changeee", command = change_text)
button.pack()


# message box
import tkinter.messagebox

def helloCallBank():
    tkinter.messagebox.showinfo("hello Python","This is the message box")

button = tkinter.Button(master,text = "Hello",command = helloCallBank)
button.pack()
button.place(height=100, width = 100)

# pack geomatry manager

# Entry
e = Entry(master)
e.pack()
def callback():  
  print (e.get())
b = Button(master, text="get", width=10, command=callback
)
b.pack()

#Label: add image

image1 = Image. open("profile.jpg")
image1 = image1.resize((250, 400))
image2 =  ImageTk. PhotoImage(image1, master = master)
image_label = tk. Label(master , image = image2)
image_label.place(x = 20 , y = 20)

#File Dialog
file_path = filedialog.askopenfilename(filetypes=[("nv232.MOV.mov",
"*.mp4;*.jpg;*.avi;*.MOV")])

# Video player
my_label_1 = Label(master)
my_label_1.pack()
player = tkvideo(file_path, my_label_1, loop = 1, size = (300,250))
player.play()




mainloop()