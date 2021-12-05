n = '\n'
myfile = open('fileProject2.txt', 'a+')

while True:
    nim = input('Masukkan NIM      : ')
    nama = input('Masukkan Nama Mhs : ')
    alamat = input('Masukkan Alamat   : ')
    
    myfile.write(f'{nim}|{nama}|{alamat}{n}')
    
    keluar = ['n', 'N']
    ask = input('Ulangi input lagi? (y/n)')
    if ask in keluar:
        break

myfile.close()