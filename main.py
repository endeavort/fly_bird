# モジュールのインポート
import tkinter  # tkinter

window = tkinter.Tk()  # ウィンドウの設定
window.title("Fly bird")  # ウィンドウのタイトル

canvas = tkinter.Canvas(width=480, height=640)  # キャンバスの設定(図形や画像の描画のため)
canvas.pack()  # キャンバスの配置

bg_img = tkinter.PhotoImage(file="img/bg.png")  # 背景画像の読み込み
player_img = tkinter.PhotoImage(file="img/bird.png")  # プレイヤー画像の読み込み

# ===========  変数  ==============
bg_posy = 0  # 背景の中心のy座標
px, py = 240, 540  # プレイヤーの位置座標（値は初期位置）

# ===========  キー操作  ==============
key = ""  # 押されたキーの値
key_off = True  # キーが押されてないフラグ

# キーが押された時
def key_down(e):
    # グローバル変数
    global key, key_off
    # keyの値を押されたキーにする
    key = e.keysym
    # キーが押されてないフラグをFalse
    key_off = False


# キーが離された時
def key_up(e):
    # グローバル変数
    global key_off
    # キーが押されてないフラグをTrue
    key_off = True


# =================================

# プレイヤーの移動処理
def move_player():
    # グローバル変数
    global px, py
    # 左キーを押す and pxが30より大きい時、pxの値を-10
    if key == "Left" and px > 30:
        px -= 10
    # 右キーを押す and pxが450より小さい時、pxの値を＋10
    if key == "Right" and px < 450:
        px += 10
    # 上キーを押す and pyが40より大きい時、pyの値を-10
    if key == "Up" and py > 40:
        py -= 10
    # 下キーを押す and pyが600より小さい時、pyの値を+10
    if key == "Down" and py < 610:
        py += 10
    # プレイヤーの描画
    canvas.create_image(px, py, image=player_img, tag="SCREEN")


# メイン処理
def main():
    # グローバル変数
    global bg_posy, key, key_off
    bg_posy = (bg_posy + 1) % 640  # 背景の中心のy座標(0~639)
    canvas.delete("SCREEN")  # キャンバス上の全てを削除
    # 背景の描画（中心のx座標, 中心のy座標, 画像, タグ)
    canvas.create_image(240, bg_posy - 320, image=bg_img, tag="SCREEN")
    canvas.create_image(240, bg_posy + 320, image=bg_img, tag="SCREEN")
    # プレイヤー処理
    move_player()
    # キーが押されていない時、キーの操作を初期値にする
    if key_off == True:
        key = ""
        key_off = False
    # 50m秒後にmainを再び実行
    window.after(50, main)


window.bind("<KeyPress>", key_down)  # キーを押した時にkey_down関数を呼び出す
window.bind("<KeyRelease>", key_up)  # キーを離した時にkey_up関数を呼び出す
main()  # メイン関数
window.mainloop()  # ウィンドウの表示
