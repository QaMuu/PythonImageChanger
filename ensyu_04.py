from tkinter import *
import tkinter.font as font

# ウィンドウの準備
root = Tk()
root.title("電卓")
root.minsize(576, 396)
root.maxsize(576, 396)

# 素材準備
pixel_virtual = PhotoImage(width=1, height=1)
font_display = font.Font(size=48, weight="bold")
font_button = font.Font(size=20, weight="bold")

# 計算用の変数
current_input = ""
first_number = 0
operation = ""

# 関数準備
def update_display(value):
    """ディスプレイの表示を更新"""
    label_display.config(text=value)

def button_click(number):
    """数字ボタンがクリックされた時の処理"""
    global current_input
    current_input += str(number)
    update_display(current_input)

def button_clear():
    """クリアボタンがクリックされた時の処理"""
    global current_input, first_number, operation
    current_input = ""
    first_number = 0
    operation = ""
    update_display("0")

def button_operation(op):
    """演算子ボタンがクリックされた時の処理"""
    global current_input, first_number, operation
    if current_input:
        first_number = float(current_input)
        current_input = ""
        operation = op
        update_display(str(first_number))

def button_equal_click():
    """イコールボタンがクリックされた時の処理"""
    global current_input, first_number, operation
    if current_input and operation:
        second_number = float(current_input)
        result = 0
        
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "×":
            result = first_number * second_number
        elif operation == "÷":
            if second_number != 0:
                result = first_number / second_number
            else:
                update_display("エラー")
                current_input = ""
                first_number = 0
                operation = ""
                return
        
        # 結果が整数の場合は小数点を表示しない
        if result == int(result):
            result = int(result)
        
        update_display(str(result))
        current_input = str(result)
        first_number = 0
        operation = ""

# ウィジェット配置
label_display = Label(
    root, 
    text = "0", 
    image = pixel_virtual, 
    compound = 'c',
    width = 384,
    height = 60,
    font = font_display,
    anchor = E)

label_display.place(x = 24, y = 24)

button_equal = Button(
    root, text = "=", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = button_equal_click)
button_equal.place(x = 432, y = 24)

button_divide = Button(
    root, text = "÷", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_operation("÷"))
button_divide.place(x = 432, y = 96)

button_multi = Button(
    root, text = "×", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_operation("×"))
button_multi.place(x = 432, y = 168)

button_subtract = Button(
    root, text = "-", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_operation("-"))
button_subtract.place(x = 432, y = 240)

button_sum = Button(
    root, text = "+", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_operation("+"))
button_sum.place(x = 432, y = 312)

button_no7 = Button(
    root, text = "7", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_click(7))
button_no7.place(x = 24, y = 96)

button_no8 = Button(
    root, text = "8", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_click(8))
button_no8.place(x = 156, y = 96)

button_no9 = Button(
    root, text = "9", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_click(9))
button_no9.place(x = 288, y = 96)

button_no4 = Button(
    root, text = "4", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_click(4))
button_no4.place(x = 24, y = 168)

button_no5 = Button(
    root, text = "5", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_click(5))
button_no5.place(x = 156, y = 168)

button_no6 = Button(
    root, text = "6", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_click(6))
button_no6.place(x = 288, y = 168)

button_no1 = Button(
    root, text = "1", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_click(1))
button_no1.place(x = 24, y = 240)

button_no2 = Button(
    root, text = "2", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_click(2))
button_no2.place(x = 156, y = 240)

button_no3 = Button(
    root, text = "3", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_click(3))
button_no3.place(x = 288, y = 240)

button_no0 = Button(
    root, text = "0", width = 252, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = lambda: button_click(0))
button_no0.place(x = 24, y = 312)

button_clear = Button(
    root, text = "C", width = 120, height = 60, image = pixel_virtual, compound = "c", font = font_button,
    command = button_clear)
button_clear.place(x = 288, y = 312)

root.mainloop()