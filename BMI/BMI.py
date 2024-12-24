
print("身長と体重でBMIを出力します。")
print("まずは、体重からです。体重を入力してください（小数点は消すか、四捨五入してください）")
taijyu = int(input("体重入力してください:")) #体重入力だよ
print("体重は",taijyu,"ですね。")
print("続いて、身長をcmで記入してください（小数点は消すか、四捨五入してください）")
shintyou = int(input("身長を入力してください（cm）："))#身長入力
print("身長は",shintyou,"ですね")
#身長をcmからメートルに変更する必要がある。
shintyou_m = shintyou / 100
#計算BMI＝体重÷（身長×身長）
BMI=taijyu/(shintyou_m*shintyou_m)
#条件
if BMI >= 40:
    print("BMIは",round(BMI),"で判定は肥満（4度）です")
    print("以上で終わります。")
elif BMI >= 35:
    print("BMIは",round(BMI),"で判定は肥満（3度）です")
    print("以上で終わります。")
elif BMI >=30:
    print("BMIは",round(BMI),"で判定は肥満（2度）です")
    print("以上で終わります。")
elif BMI >=25:
    print("BMIは",round(BMI),"で判定は肥満（1度）です")
    print("以上で終わります。")
elif BMI >=18:
    print("BMIは",round(BMI),"で判定は普通です")
    print("以上で終わります。")
else:
    print("BMIは",round(BMI),"で判定は痩せすぎです")
    print("以上で終わります。")
    