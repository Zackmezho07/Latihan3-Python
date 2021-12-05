n = '\n'
myfile = open('fileProject2.txt', 'r')

dataTotal = []

myfile.seek(0)
eachLine = myfile.readlines()
for i in range(len(eachLine)):
    semuaData = {}
    data = eachLine[i].replace('\n', '')
    dataMhs = data.split('|')
    semuaData['nim']=dataMhs[0]
    semuaData['nama']=dataMhs[1]
    semuaData['alamat']=dataMhs[2]
    dataTotal.append(semuaData)
myfile.close()

cari = input('Masukkan NIM yang mau dicari : ')

for i in range(len(dataTotal)):
    nimMhs = dataTotal[i]['nim']
    if nimMhs in cari:
        print('Data Mahasiswa :')
        print('NIM      : ', dataTotal[i]['nim'])
        print('Nama     : ', dataTotal[i]['nama'])
        print('Alamat   : ', dataTotal[i]['alamat'])
        break
    else:
        print('Data mahasiswa tidak ditemukan')
        break
