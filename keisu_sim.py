from tqdm import tqdm

main_data = ['T25B201G', 'T25B202E', 'T25B203C', 'T25B204A', 'T25B205K', 'T25B206H', 'T25B207F', 'T25B208D', 'T25B209B', 'T25B210F', 'T25B211D', 'T25B212B', 'T25B213A', 'T25B214J', 'T25B215G', 'T25B216E', 'T25B217C', 'T25B218A', 'T25B219K', 'T25B220C', 'T25B221A',] 
matubi_suji = [6, 4, 2, 0, 9, 7, 5, 3, 1, 5, 3, 1, 0, 8, 6, 4, 2, 0, 9, 2, 0,] 

#Tと末尾を抜いて，Bを変換
def conv(e):
    result = '25'+'1'+e[4]+e[5]+e[6]
    return result

converted_data = list(map(conv, main_data))

#シュミレート(一括)
def simulate1():
    sum = []
    sumtemp = 0
    bar = tqdm(total=900000)
    ff = open('log4bulk.txt', 'x')

    for i in range(100000, 1000000):
        ii = str(i).zfill(6)
        for j in converted_data:
            for e in range(6):
                temp = (int(j[e]))*(int(ii[e]))
                sumtemp = sumtemp + temp
            sumtemp2 = (int(sumtemp) % 10)
            if sumtemp2 == 0:
                sum.append(0)
            elif not(sumtemp2 == 0):
                sum.append(10 - sumtemp2)
            sumtemp = 0

        ff.write(str(ii)+str(sum)+'\n')
        if sum == matubi_suji:
            print('係数は'+ii)
            break
        if i == 999999:
            print('あてはまる係数は存在しませんでした。')
        
        sum.clear()
        bar.update(1)
    ff.close()



#シュミレート（分割）
def simulate2():
    sum = []
    sumtemp = 0
    bar = tqdm(total=900000)
    f = open('log4spl.txt','x')

    for i in range(100000, 1000000):
        ii = str(i).zfill(6)
        for j in converted_data:
            for e in range(6):
                temp = (int(j[e]))*(int(ii[e]))
                if len(str(temp)) == 1:
                    sumtemp = sumtemp + temp
                elif len(str(temp)) == 2:
                    temp2 = int(str(temp)[1]) + int(str(temp)[0])
                    sumtemp = sumtemp + temp2
            sumtemp2 = (int(sumtemp) % 10)
            if sumtemp2 == 0:
                sum.append(0)
            elif not(sumtemp2 == 0):
                sum.append(10 - sumtemp2)
            sumtemp = 0

        f.write(str(ii)+str(sum)+'\n')
        if sum == matubi_suji:
            print('係数は'+ii)
            break

        if i == 999999:
            print('あてはまる係数は存在しませんでした。')
        
        sum.clear()
        bar.update(1)
    f.close()


simulate1()
simulate2()