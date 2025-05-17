import deff

#n1 : 元データ
#n2 : 末尾の使われている文字ソートデータ
#n3 : 末尾のみデータ
#n4 : 末尾数字変換配列
#n5 : 三桁和

datafilepass = "./data.txt"

n1 = deff.start(datafilepass)
n2 = deff.unexiststr(n1)
n3 = deff.matubi(n1)
n4 = deff.number_convert(n3, n2)
n5 = deff.sum(n1)

cov = []

for h in n4:
    cov.append(h*0.0064 + 4.013)
print(cov)