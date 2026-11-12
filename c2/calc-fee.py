# BMI判定プログラム
weight = float(input("体重(kg)は？"))
height = float(input("身長(cm)は？"))
# BMIの計算
height = height / 100 # m に直す
bmi = weight / (height * height)
# BMIの値に応じて結果を分岐
result = ""
if bmi < 18.5 :
    result = "瘦せ型"
if (18.5 =< bmi) and (bmi < 25) :
    result = "標準体型"