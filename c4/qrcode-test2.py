# パッケージをインポート
import qrcode
import random

arList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
word = ""

for i in range(1, 2000):
    r = random.randint(1, 13)
    word = word + arList[r]
# QRコードを生成
img = qrcode.make(word)
# ファイルに保存
img.save("qrcode-test2.png")