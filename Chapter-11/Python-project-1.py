from datetime import *

def diffDate(x):
    tanggalSelisih = datetime.strptime(x, '%Y-%m-%d')
    tanggalSekarang = datetime.now()
    delta = tanggalSekarang - tanggalSelisih
    a = delta.days
    return a

selisih = diffDate('2021-12-7')
print(selisih)