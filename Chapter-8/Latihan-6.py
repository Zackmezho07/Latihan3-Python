malis = ['a', 'aaaaaa', 'aks', 'ssss']

def sortStringByChar(x):
    for i in range(len(x)):
        for j in range(len(x) - i -1):
            if len(x[j]) < len(x[j + 1]):
                x[j], x[j + 1] = x[j + 1], x[j]
    return x

print(sortStringByChar(malis))