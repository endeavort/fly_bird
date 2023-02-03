# モジュールのインポート
import tkinter  # tkinter

window = tkinter.Tk()  # ウィンドウの設定
window.title("Fly bird")  # ウィンドウのタイトル

canvas = tkinter.Canvas(width=480, height=640)  # キャンバスの設定(図形や画像の描画のため)
canvas.pack()  # キャンバスの配置

bg_img = tkinter.PhotoImage(file="img/bg.png")  # 背景画像の読み込み

# ===========  変数  ==============
bg_posy = 0

# メイン処理
def main():
    # グローバル変数
    global bg_posy
    bg_posy = (bg_posy + 1) % 640  # 背景の中心のy座標(0~639)
    canvas.delete("SCREEN")  # キャンバス上の全てを削除
    # 背景の描画（中心のx座標, 中心のy座標, 画像, タグ)
    canvas.create_image(240, bg_posy - 320, image=bg_img, tag="SCREEN")
    canvas.create_image(240, bg_posy + 320, image=bg_img, tag="SCREEN")
    # 50m秒後にmainを再び実行
    window.after(50, main)


main()  # メイン関数
window.mainloop()  # ウィンドウの表示
