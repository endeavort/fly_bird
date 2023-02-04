# モジュールのインポート
import tkinter  # tkinter
import random  # ランダム

window = tkinter.Tk()  # ウィンドウの設定
window.title("Fly bird")  # ウィンドウのタイトル

canvas = tkinter.Canvas(width=480, height=640)  # キャンバスの設定(図形や画像の描画のため)
canvas.pack()  # キャンバスの配置

# 画像の読み込み
bg_img = tkinter.PhotoImage(file="img/bg.png")  # 背景
player_img = tkinter.PhotoImage(file="img/bird.png")  # プレイヤー
thunder_img = tkinter.PhotoImage(file="img/thunder.png")  # 雷
gameover_img = tkinter.PhotoImage(file="img/gameover.png")  # ゲームオーバー

# フォントの読み込み
small_font = ("Times New Roman", 24)  # フォント小
large_font = ("Times New Roman", 50)  # フォント大

# ===========  定数  ==============
THUNDER_MAX = 30  # 雷の最大数
THUNDER_SPEED = 6  # 雷の落下速度レベル（THUNDER_MAX~1の範囲,1に近づくにつれ難易度up)

# ===========  変数  ==============
bg_posy = 0  # 背景の中心のy座標
px, py = 240, 540  # プレイヤーの位置座標（値は初期位置）
tx, ty = [0] * THUNDER_MAX, [0] * THUNDER_MAX  # 雷の位置座標（最大数分）
phase = 0  # フェーズ
# 0:タイトル
# 1:ゲームプレイ中
# 2:ゲームオーバー
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


# 初期設定
def game_init():
    # グローバル変数
    global px, py
    px, py = 240, 540  # プレイヤー初期位置
    # 雷初期位置
    for i in range(THUNDER_MAX):
        tx[i] = random.randint(0, 480)  # x座標を0~480の範囲でランダムに決める
        ty[i] = random.randint(-640, 0)  # y座標を-640~0の範囲でランダムに決める


# 雷の移動処理
def move_thunder():
    global phase
    for i in range(THUNDER_MAX):
        ty[i] += 6 + i / THUNDER_SPEED  # 雷のy座標をレベルに分けて増やす
        if ty[i] > 660:
            tx[i] = random.randint(0, 480)  # x座標を0~480の範囲でランダムに決める
            ty[i] = random.randint(-640, 0)  # y座標を-640~0の範囲でランダムに決める
        # 　プレイヤーと雷が接触したらゲームオーバーへ
        if hit_thunder(px, py, tx[i], ty[i]):
            phase = 2
        # 雷の描画
        canvas.create_image(tx[i], ty[i], image=thunder_img, tag="SCREEN")


# 接触判定
def hit_thunder(x1, y1, x2, y2):
    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) < 36**2:
        return True
    return False


# メイン処理
def main():
    # グローバル変数
    global bg_posy, key, key_off, phase
    bg_posy = (bg_posy + 1) % 640  # 背景の中心のy座標(0~639)
    canvas.delete("SCREEN")  # キャンバス上のSCREENタグの画像を全て削除
    # 背景の描画（中心のx座標, 中心のy座標, 画像, タグ)
    canvas.create_image(240, bg_posy - 320, image=bg_img, tag="SCREEN")
    canvas.create_image(240, bg_posy + 320, image=bg_img, tag="SCREEN")
    # タイトル画面時
    if phase == 0:
        # テキストの描画(中心のx座標, 中心のy座標, テキスト, 色, フォント, タグ)
        canvas.create_text(
            240, 240, text="Fly Bird", fill="darkblue", font=large_font, tag="SCREEN"
        )
        canvas.create_text(
            240,
            480,
            text="Press [SPACE] Key",
            fill="darkblue",
            font=large_font,
            tag="SCREEN",
        )
        # スペースキーが押された時
        if key == "space":
            game_init()  # ゲーム初期化処理
            phase = 1  # フェーズをゲームプレイ中に

    # ゲームプレイ中の時
    if phase == 1:
        # プレイヤー処理
        move_player()
        # 雷処理
        move_thunder()

    # ゲームオーバーの時
    if phase == 2:
        move_thunder()
        canvas.create_image(px, py, image=gameover_img, tag="SCREEN")
        canvas.create_text(
            240, 240, text="GAME OVER", fill="red", font=large_font, tag="SCREEN"
        )

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
