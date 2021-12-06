from datetime import *
n = '\n'
myfile = open('fileProject2.txt', 'a')

while True:
    kode = input('Masukkan Kode Member  : ')
    nama = input('Masukkan Nama Member  : ')
    buku = input('Masukkan Judul Buku   : ')
    peminjaman = datetime.date(datetime.today())
    pengembalian = peminjaman + timedelta(days=7)
    dataList = f'{kode}|{nama}|{buku}|{peminjaman}|{pengembalian}{n}'
    myfile.write(dataList)

    reject = ['n', 'N']
    ask = input('Ulangi lagi? (y/n)')
    if ask in reject:
        break

myfile.close()
