# 辞書型のデータ（果物名と値段）を変数に代入
fruits = {
    "バナナ" : 300,
    "オレンジ" : 240,
    "イチゴ" : 350,
    "マンゴー" : 400
}

# 辞書型のデータ一覧を表示
for name, price in fruits.items() :
    # 値段を得る
    price = fruits[name]
    # 画面に出力
    s = f"{name}は、{price}円です。"
    print(s)