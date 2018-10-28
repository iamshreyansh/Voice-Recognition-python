from Tkinter import *
from PIL import ImageTk

canvas = Canvas(width = 200, height = 200, bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)

image = ImageTk.PhotoImage(file = "C:/Python27/programas/zimages/gato.png")
canvas.create_image(10, 10, image = image, anchor = NW)

mainloop()
