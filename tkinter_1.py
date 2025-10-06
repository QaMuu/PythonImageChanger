from tkinter import *

# ウィンドウの準備
root = Tk()
root.title("ボタン設置")
root.minsize(400, 200)
root.maxsize(400, 200)

label_message = Label(root, text = "Hello!")
label_message.pack()

def change_message():
    get_name = entry_message.get()
    label_message["text"] = "こんにちわ、" + get_name + "！"
    entry_message.delete(0, END)

button_message = Button(root, text = "Message", command = change_message)
button_message.pack()

entry_message = Entry(root)
entry_message.pack()

def close_window():
    root.destroy()

button_end = Button(root, text = "End", command = close_window)
button_end.pack()

root.mainloop()