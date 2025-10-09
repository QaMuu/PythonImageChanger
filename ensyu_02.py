from tkinter import *

# ウィンドウの準備
root = Tk()
root.title("画像表示")
root.minsize(400, 200)
root.maxsize(400, 200)

image_cat = PhotoImage(width=160, height=160, file = "cat.png")

label_cat = Label(
  root,
  image = image_cat,
  width = 160,
  height = 160,
  )

label_cat.pack()

root.mainloop()