
def dataStat(x):
    jml = 0
    for i in x:
        jml += i
    rerata = jml / len(x)
    dataSet = tuple(x)
    maks = max(dataSet)
    mins = min(dataSet)
    
    myList = []
    myList.append(rerata)
    myList.append(maks)
    myList.append(mins)
    return myList

listapapun = [2, 3, 4, 5, 6, 7, 8, 9]
a = dataStat(listapapun)

print(a)