# モジュールのインポート
import tkinter  # tkinter

window = tkinter.Tk()  # ウィンドウの設定
window.title("Fly bird")  # ウィンドウのタイトル

canvas = tkinter.Canvas(width=480, height=640)  # キャンバスの設定(図形や画像の描画のため)
canvas.pack()  # キャンバスの配置

window.mainloop()  # ウィンドウの表示
