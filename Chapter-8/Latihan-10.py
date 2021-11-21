buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
for i in buah:
    print(i)

totalHarga = 0
while True:
    nama = input('Nama buah yang dibeli : ')
    kg =   int(input('Berapa Kg?           : '))
    a = buah[nama]
    b = a*kg
    totalHarga += b
    inp = input('Beli buah yang lain? (y/n)')
    keluar = ['n', 'N']
    if inp in keluar:
        break

print('----------------------')
print(f'Total harga         :{totalHarga}')