buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def beliBuah(arr):
    totalHarga = 0
    while True:
        nama = input('Nama buah yang dibeli : ')
        kg =   int(input('Berapa Kg?           : '))
        a = arr[nama]
        b = a*kg
        totalHarga += b
        inp = input('Beli buah yang lain? (y/n)')
        keluar = ['n', 'N']
        if inp in keluar:
            break
    return totalHarga

print('Menu :')
print('A. Tambah data buah')
print('B. Beli buah')
print('C. Hapus data buah')

pil = input('Pilihan menu : ')

if pil == 'A':
    namaBuah = input('Masukkan nama buah    : ')
    harga = input('Masukkan harga satuan : ')
    buah[namaBuah] = harga
    for x,y in buah.items():
        print(f'{x} (harga Rp {y})')
elif pil == 'B':
    total = beliBuah(buah)
    print('-------------------------------')
    print(f'Total harga          : {total}')
elif pil == 'C':
    for x,y in buah.items():
        print(f'{x} (harga Rp {y})')
    hapusBuah = input('Nama buah yang akan di hapus : ')
    if hapusBuah in buah:
        del buah[hapusBuah]
        print(f'Buah {hapusBuah} berhasil dihapus dari daftar')
    else:
        print('Nama buah tidak ditemukan')
    for x,y in buah.items():
        print(f'{x} (harga Rp {y})')
else:
    print('Pilihan tidak tersedia')