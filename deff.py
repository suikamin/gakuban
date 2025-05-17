from tqdm import tqdm

#文字列を余分なものをのぞいて配列に変換
def start(e):
    lf = open(e, 'r', encoding='UTF-8')
    data = lf.read()
    lf.close()

    rsltalley = []
    
    alley = data.split()
    for ii in alley:
        if "T25B" in ii:
            rsltalley.append(ii)
    
    rsltalley.sort()

    return rsltalley

# 末尾に存在しない文字を列挙
def unexiststr(n):
    o = []

    for r in n:
        if not(r[7] in o):
            o.append(r[7])

    o.sort()

    return o

def matubi(q):
    s = []
    for w in q:
        s.append(w[7])
    return s 

#10個ずつ配列を表示
def print10(a):
    i = 0
    l = []

    for k in a:
        l.append(k)
        i = i + 1
        if i % 10 == 0:
            print(l)
            l.clear()

#アルファベットを数字に変換
def number_convert(p,pp):
    rslt = []
    for d in p:
        rslt.append(int(pp.index(d)))
    return rslt

#割っている数を探す
def mod(n1, n4):
    bar = tqdm(total=900)
    bar.set_description('Modulo progress...')

    sumalley = []
    modrslt = []

    for i in range(9):
        for m in n1:
            sum = i + int(m[4]) + int(m[5]) + int(m[6])
            sumalley.append(sum)

        for a in range(100):
            for b in sumalley:
                modrslt.append(int(b % (a+1)))
            bar.update(1)
            if  n4 == modrslt:
                print('Correct modulo number is' + a)
                break
        
        sumalley.clear()


    return sumalley

#単純に3桁を足す
def sum(a):
    sumalley = []
    for m in a:
        su = int(m[4]) + int(m[5]) + int(m[6])
        sumalley.append(su)
    return sumalley

#12-2xsum
def calculate(e , e2):
    bar = tqdm(total=170)
    bar.set_description('Progress')

    k = []

    for i in e:
        k.append(i * 2)
        bar.update(1)
    
    return k