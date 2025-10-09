from tkinter import *

# ウィンドウの準備
root = Tk()
root.title("ボタン設置")
root.minsize(400, 200)
root.maxsize(400, 200)

pixel_virtual = PhotoImage(width=1, height=1)

button = Button(
  root,
  text = "place test", 
  image = pixel_virtual,
  width = 100,
  height = 50,
  compound='c')
button.place(x = 200, y = 100)

root.mainloop()