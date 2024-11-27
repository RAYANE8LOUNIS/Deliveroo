import tkinter as tk 
from tkinter import Canvas
from tkinter import PhotoImage
window = tk.Tk()
window.geometry("800x600")

canvas =tk.Canvas(window, width =800 , height =600)
canvas.pack()

img = PhotoImage(file = "delivroo.png")
canvas.create_image(0,0, anchor="nw" , image=img)
window.mainloop()