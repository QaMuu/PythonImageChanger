from tkinter import *
import random

# ウィンドウの準備
root = Tk()
root.title("じゃんけんゲーム")
root.minsize(456, 600)
root.maxsize(456, 600)

# 素材準備
pixel_virtual = PhotoImage(width=1, height=1)

image_enemy_empty = PhotoImage(width = 120, height = 120, file = "enemy_empty.png")
image_enemy_rock = PhotoImage(width = 120, height = 120, file = "enemy_rock.png")
image_enemy_scissors = PhotoImage(width = 120, height = 120, file = "enemy_scissors.png")
image_enemy_paper = PhotoImage(width = 120, height = 120, file = "enemy_paper.png")
list_image_enemy_hand = [image_enemy_rock, image_enemy_scissors, image_enemy_paper]

image_player_empty = PhotoImage(width = 120, height = 120, file = "player_empty.png")
image_player_rock = PhotoImage(width = 120, height = 120, file = "player_rock.png")
image_player_scissors = PhotoImage(width = 120, height = 120, file = "player_scissors.png")
image_player_paper = PhotoImage(width = 120, height = 120, file = "player_paper.png")
list_image_player_hand = [image_player_rock, image_player_scissors, image_player_paper]

# 関数準備
def fight_rsp(player_hand):
    enemy_hand = random.randint(0,2)

    result = (player_hand - enemy_hand + 3) % 3

    result_text = ""
    if result == 0:
        result_text = "あいこでした！"
    elif result == 2:
        result_text = "あなたの勝ち！"
    else: # result == 1
        result_text = "あなたの負け…"
    
    label_fight["text"] = result_text
    label_enemy_hand["image"] = list_image_enemy_hand[enemy_hand]
    label_player_hand["image"] = list_image_player_hand[player_hand]

def click_rock():
    fight_rsp(0)

def click_scissors():
    fight_rsp(1)

def click_paper():
    fight_rsp(2)

def click_retry():
    label_fight["text"] = "じゃんけん！"
    label_enemy_hand["image"] = image_enemy_empty
    label_player_hand["image"] = image_player_empty

# ウィジェット配置

# 敵の手役を表示するラベルを、x = 168, y = 48に配置します。サイズは 120 × 120です。
label_enemy_hand = Label(root, image = image_enemy_empty, width = 120, height = 120)
label_enemy_hand.place(x = 168, y = 48)

# 勝敗を表示するラベルを、x = 24, y = 200に配置します。サイズは 408 × 36です。
label_fight = Label(root, text = "じゃんけん！", width = 408, height = 36, image = pixel_virtual, compound = "c")
label_fight.place(x = 24, y = 200)

# プレイヤーの表示するラベルを、x = 168, y = 266に配置します。サイズは 120 × 120です。
label_player_hand = Label(root, image = image_player_empty, width = 120, height = 120)
label_player_hand.place(x = 168, y = 266)

# ✊️のボタンを、x = 24, y = 432に配置します。サイズは 120 × 60です。
button_rock = Button(root, text = "✊️", width = 120, height = 60, image = pixel_virtual, compound = "c", command = click_rock)
button_rock.place(x = 24, y = 432)

# ✌️のボタンを、x = 168, y = 432に配置します。サイズは 120 × 60です。
button_scissors = Button(root, text = "✌️", width = 120, height = 60, image = pixel_virtual, compound = "c", command = click_scissors)
button_scissors.place(x = 168, y = 432)

# 🖐️のボタンを、x = 312, y = 432に配置します。サイズは 120 × 60です。
button_paper = Button(root, text = "🖐️", width = 120, height = 60, image = pixel_virtual, compound = "c", command = click_paper)
button_paper.place(x = 312, y = 432)

# 【もう一度！】のボタンを、x = 168, y = 516に配置します。サイズは 120 × 60です。
button_retry = Button(root, text = "もう一度！", width = 120, height = 60, image = pixel_virtual, compound = "c", command = click_retry)
button_retry.place(x = 168, y = 516)

root.mainloop()