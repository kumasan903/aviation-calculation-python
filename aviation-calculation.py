import tkinter as tk
import math

# ボタンを押したときの処理
def calc_dist():
    # 取得
    cra = float(CurrentAlt.get()) * 100  # CurrentAltitude
    toa = float(DecendTo.get()) * 100    # toAltitude
    pas = float(DecendPass.get())        # pass

    # 差分を計算
    dif = cra - toa # difference

    # 必要距離を計算
    distft = dif / math.tan(math.radians(pas))
    distnm = distft / 6076 # 海里に変換

    # 結果をラベルに表示
    s = "高度差：" + str(round(dif)) + "ft." + " 必要距離：" + str(round(distnm,1)) + "nm."
    labelResult['text'] = s

# ウィンドウを作成
win = tk.Tk()
win.title("降下計算")
win.geometry("250x200")

# 部品を作成
# 現在高度
labelCurrentAlt = tk.Label(win, text=u'現在高度(FL)')
labelCurrentAlt.pack()

CurrentAlt = tk.Entry(win)
CurrentAlt.insert(tk.END, '380')
CurrentAlt.pack()

# 降下目標高度
labelDecendTo = tk.Label(win, text=u'降下目標高度(FL)')
labelDecendTo.pack()

DecendTo = tk.Entry(win)
DecendTo.insert(tk.END, '180')
DecendTo.pack()

# 降下パス()
labelDecendPass = tk.Label(win, text=u'降下パス(度)')
labelDecendPass.pack()

DecendPass = tk.Entry(win)
DecendPass.insert(tk.END, '3')
DecendPass.pack()

# 計算結果
labelResult = tk.Label(win, text=u'---')
labelResult.pack()

# 計算ボタン
calcButton = tk.Button(win, text=u'計算')
calcButton["command"] = calc_dist
calcButton.pack()

# ウィンドウを動かす
win.mainloop()