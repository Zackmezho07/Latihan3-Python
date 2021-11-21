def kuadrat(bil):
    yoList = []
    for i in range(len(bil)):
        kua = bil[i]
        drat = kua ** 2
        yoList.append(drat)
    return yoList

malist = [2, 3, 4, 5, 6]
s = kuadrat(malist)
print(s)