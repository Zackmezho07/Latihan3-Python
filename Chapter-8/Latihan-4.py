dataSayur = ['bayam', 'kangkung', 'wortel', 'selada']

def programSayur():
    print(dataSayur)
    print('Menu :')
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilkan data sayur')
    inp = input('Pilihan Anda :.....')
    if inp == 'A':
        a = input('Masukkan nama sayur :')
        dataSayur.append(a)
    elif inp == 'B':
        try:
            b = input('Masukkan nama sayur yang ingin di hapus : ')
            dataSayur.remove(b)
        except:
            print('Data yang ingin dihapus tidak ada')
    elif inp == 'C':
        print(dataSayur)
    else:
        print('Input anda salah')

while True:
    programSayur()
    print(dataSayur)
    y = input('Masukkan lagi? (y/n)')
    keluar = ['n', 'N']
    if y in keluar:
        break