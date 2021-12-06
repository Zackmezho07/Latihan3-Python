from datetime import *
n = '\n'
myfile = open('fileProject2.txt', 'r')

mylist = []
listcode = []
search = input('Masukkan Kode Member : ')
eachData = myfile.readlines()

for i in range(len(eachData)):
    rem = eachData[i].replace('\n', '')
    dataPerpus = rem.split('|')
    mylist.append(dataPerpus)

for i in range(len(mylist)):
    codePerpus = mylist[i][0]
    listcode.append(codePerpus)

if search in listcode:
    i = listcode.index(search)
    kode = mylist[i][0]
    nama = mylist[i][1]
    buku = mylist[i][2]
    peminjaman = mylist[i][3]
    makskembali = mylist[i][4]
    
    tanggalPinjam = datetime.date(datetime.strptime(peminjaman, '%Y-%m-%d'))
    tanggalsekarang = datetime.date(datetime.today())
    delta = tanggalPinjam - tanggalsekarang
    selisih = int(delta.days)
    
    if selisih > 0:
        denda = selisih * 2000
    else:
        denda = '-'

    print(f'Kode Member                 : {kode}')
    print(f'Nama Member                 : {nama}')
    print(f'Judul Buku                  : {buku}')
    print(f'Tanggal Mulai Peminjaman    : {peminjaman}')
    print(f'Tanggal Maks peminjaman     : {makskembali}')
    print(f'Terlambat                   : {selisih} days')
    print(f'Denda                       : Rp {denda}')
else:
    print('tidak ada data yang ditemukan')


myfile.close()