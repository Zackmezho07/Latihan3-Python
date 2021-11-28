import random

def shuffleString(x,n):
    result = []
    mylist = list(x)
    nilaiMax = 1
    for i in range(1, len(x) + 1):
        nilaiMax *= i
    if n > nilaiMax:
        n  = nilaiMax
    for i in range(n):
        while True:
            random.shuffle(mylist)
            hasil = ''.join(mylist)
            if hasil in result:
                continue
            elif hasil not in result:
                result.append(hasil)
                break
    return result

a = shuffleString('myBrainsHurt', 5)
print(a)