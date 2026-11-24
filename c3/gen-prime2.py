# 素数を返すイテレータ
def genPrime(maxnum):
    num = 2
    primeList = []
    while (num <= maxnum):
        is_prime = True     # 素数かどうかを管理する変数を定義
        for i in range(2, num):     # numが2の時は範囲に含まれる値がなく実行されない
            if(num % i) == 0: # 素数ではない
                is_prime = False
                break
            else: 
                yield num
                primeList.append(num)
        num += 1

# イテレータを得る
it = genPrime(500)

# 画面に出力
for i in it:
    print(i, end=",")