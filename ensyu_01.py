from tkinter import *

# ウィンドウの準備
root = Tk()
root.title("ボタン設置")
root.minsize(400, 200)
root.maxsize(400, 200)

list_message = ["こんにちは", "Hello", "안녕하세요"]
list_language = ["日本語", "英語", "韓国語"]

label_message = Label(root, text = list_message[0])
label_message.pack()

def change_message(target_num):
    label_message["text"] = list_message[target_num]

def change_japanese():
    change_message(0)

button_japanese = Button(root, text = list_language[0], command = change_japanese)
button_japanese.pack()

def change_english():
    change_message(1)

button_english = Button(root, text = list_language[1], command = change_english)
button_english.pack()

def change_korean():
    change_message(2)

button_korean = Button(root, text = list_language[2], command = change_korean)
button_korean.pack()

root.mainloop()