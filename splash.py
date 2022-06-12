# Import module
from tkinter import *
import multiprocessing, time

# Create object
root = Tk()
root.after(3000, lambda: root.destroy())
root.eval("tk::PlaceWindow . center")
root.overrideredirect(True)
root.wm_geometry("315x297")

canvas = Canvas(root, width=315, height=297)
canvas.pack()
img = PhotoImage(file="d20.png")
canvas.create_image(0, 0, anchor=NW, image=img)

# Execute tkinter
root.mainloop()
